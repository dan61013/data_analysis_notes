"""
Data Visualization: 製作多學系不同入學管道折線圖(大一到大四)

參考資料:
1. Quick Guide: https://matplotlib.org/stable/users/explain/quick_start.html
2. CSS Colors: https://matplotlib.org/stable/gallery/color/named_colors.html#css-colors
3. Line Plot Reference: https://steam.oxxostudio.tw/category/python/example/matplotlib-line-plot.html
4. plot Reference: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot
5. plot marker: https://matplotlib.org/stable/api/markers_api.html
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def get_grade_1_to_4_mean(df, inschool_list: list):
    """計算學系大一到大四的學生平均成績

    Args:
        df (pandas.DataFrame): 學系全部學生的成績資料\n
        inschool_list (list): 入學管道清單

    Returns:
        List: 該學系學生大一到大四的平均成績
    """
    df_inschool = df[df["入學方式"] == inschool_list[0]]
    dept_grade_1 = df_inschool["大一平均分數"].mean()
    dept_grade_2 = df_inschool["大二平均分數"].mean()
    dept_grade_3 = df_inschool["大三平均分數"].mean()
    dept_grade_4 = df_inschool["大四平均分數"].mean()
    return [dept_grade_1, dept_grade_2, dept_grade_3, dept_grade_4]

def main():
    # Load DataFrame
    df = pd.read_excel("./test.xlsx", sheet_name="sheet1")
    # Filter
    df = df[df["學分數"] > 127]
    # 取得入學管道名稱 & 學系名稱清單
    inschool_list = df["入學方式"].drop_duplicates().to_list()
    dept_list = df["學系名稱"].drop_duplicates().to_list()
    # 設定X bar
    x_axis = ["大一", "大二", "大三", "大四"]
    # 設定字形
    matplotlib.rc("font", family="Microsoft JhengHei")

    # 迴圈(每個學系)
    for dept in dept_list:
        df_dept = df[df["學系名稱"] == dept]
        fig, ax = plt.subplots(figsize=(10, 5), layout="constrained")

        # 五種入學管道，如果該學系沒有此入學管道，則pass
        # 入學管道1
        if inschool_list[0]:
            ax.plot(x_axis, get_grade_1_to_4_mean(df_dept, inschool_list[0]),
                     color="royalblue",
                     linewidth=3,
                     marker=".",
                     markersize=15,
                     label=inschool_list[0])
        else:
            pass

        # 入學管道2
        if inschool_list[1]:
            ax.plot(x_axis, get_grade_1_to_4_mean(df_dept, inschool_list[1]),
                     color="olivedrab",
                     linewidth=3,
                     marker=".",
                     markersize=15,
                     label=inschool_list[1])
        else:
            pass

        # 入學管道3
        if inschool_list[2]:
            ax.plot(x_axis, get_grade_1_to_4_mean(df_dept, inschool_list[2]),
                     color="darkorange",
                     linewidth=3,
                     marker=".",
                     markersize=15,
                     label=inschool_list[2])
        else:
            pass

        # 入學管道4
        if inschool_list[3]:
            ax.plot(x_axis, get_grade_1_to_4_mean(df_dept, inschool_list[3]),
                     color="brown",
                     linewidth=3,
                     marker=".",
                     markersize=15,
                     label=inschool_list[3])
        else:
            pass

        # 入學管道5
        if inschool_list[4]:
            ax.plot(x_axis, get_grade_1_to_4_mean(df_dept, inschool_list[4]),
                     color="slategray",
                     linewidth=3,
                     marker=".",
                     markersize=15,
                     label=inschool_list[4])
        else:
            pass

        # 設定圖表標題、XY軸標題
        ax.set_title(dept)
        ax.set_xlabel("就讀年級")
        ax.set_ylabel("平均成績")
        # Reference: https://blog.csdn.net/humingzhu_97/article/details/104899572
        ax.legend()  # loc="upper left"
        # plt.show()

        # 儲存PNG
        plt.savefig(f"./output/data_visualization/{dept}.png")

if __name__ == "__main__":
    main()
