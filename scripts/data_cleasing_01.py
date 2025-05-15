"""
data_cleansing_01: 篩選學生修課資料與成績，並和基本資料合併。
"""

import numpy as np
import pandas as pd

STUDENT_SCORE = "./docs/105-110_學生修課資料與成績.dta"
STUDENT_INFO = "./docs/105-110_學生基本資料.dta"

def main():
    """腳本執行
    """
    # Load DataFrame
    df = pd.read_stata(STUDENT_SCORE)
    df_student_info = pd.read_stata(STUDENT_INFO)

    # filter
    df = df.drop_duplicates(subset=["學號", "課號", "成績"])
    df = df[df["學制名稱"] == "四年制大學部"]
    df = df[df["入學方式"].isin(["推薦甄試", "聯合招生", "申請入學", "繁星計畫入學", "技優甄審入學"])]
    df = df[df["成績"] >= 0]
    df["修課學期"] = df["修課學期"].astype(str)
    df = df[df["修課學期"].isin(["1", "2"])]

    # 取得/新增入學年度
    inschool = []
    for i in df["學號"]:
        if len(i) == 8:
            inschool.append(i[:2])
        else:
            inschool.append(i[:3])
    df.insert(0, "入學年度", inschool)
    df["入學年度"] = df["入學年度"].astype(str)

    # filter: 入學年度 107 to 109
    df = df[df["入學年度"].isin(["107", "108", "109"])]

    # 調整入學方式字串
    df["入學方式"] = df["入學方式"].replace(
            {
                "推薦甄試": "甄選入學",
                "聯合招生": "聯合登記分發",
                "申請入學": "四技申請入學"
            }
        )

    # 新增就讀年級(依班級名稱)
    grade_list = ["大一", "大二", "大三", "大四"]
    for i in grade_list:
        df.loc[df["班級名稱"].str.contains(i[-1]), "就讀年級"] = i

    # 合併分組名稱/畢業學校/畢業系所
    df_merge = pd.merge(df, df_student_info[["學號", "分組名稱", "畢業學校", "畢業系所"]], how="inner", on=["學號"])

    # 計算學生修讀每一堂課程的排名與PR值
    df_course_count_dict = df_merge.groupby("課號")["學號"].count().to_dict()
    df_merge["課號計數"] = df_merge["課號"].map(df_course_count_dict)
    df_merge["課程排名"] = df_merge.groupby("課號")["成績"].rank(method="dense", ascending=False)
    df_merge["課程PR"] = ((df_merge["課號計數"] - df_merge["課程排名"]) / df_merge["課號計數"]) * 100
    df_merge["課程PR"] = df_merge["課程PR"].apply(lambda x: np.round(x, 1))

    # 計算學生每一年級的課程總平均PR值
    df_student_course_average_pr = df_merge.groupby(["入學年度", "學號", "就讀年級"])\
        .agg(student_course_average_pr=pd.NamedAgg(column="課程PR", aggfunc="mean"))
    df_merge = pd.merge(df_merge,
                        df_student_course_average_pr,
                        on=["入學年度", "學號", "就讀年級"],
                        how="inner")
    df_merge["student_course_average_pr"] = df_merge["student_course_average_pr"].\
        apply(lambda x: np.round(x, 1))

    # 使用學生每一年級的課程總平均PR值，計算系排名與PR值
    df_dept_student_count = df_merge.drop_duplicates(subset=["入學年度", "就讀年級", "學號"]).\
        groupby(["入學年度", "系所名稱", "就讀年級"], as_index=False)["學號"].count()
    df_dept_student_count.rename({"學號": "學系該年級學生人數"}, axis="columns", inplace=True)
    df_merge = pd.merge(df_merge, df_dept_student_count, on=["入學年度", "系所名稱", "就讀年級"], how="inner")
    df_merge["該年級系排名"] = df_merge.groupby(["入學年度", "系所名稱", "就讀年級"])["student_course_average_pr"].\
        rank(method="dense", ascending=False)
    df_merge["該年級系PR"] = ((df_merge["學系該年級學生人數"]-df_merge["該年級系排名"])/df_merge["學系該年級學生人數"])*100
    df_merge["該年級系PR"] = df_merge["該年級系PR"].apply(lambda x: np.round(x, 1))

    # 去除重複值
    df_merge.drop_duplicates(subset=["入學年度", "就讀年級", "學號"], inplace=True)

    df_merge.to_csv("./data_cleansing.csv",
                    encoding="utf-8-sig",
                    index=False)

if __name__ == "__main__":
    main()
