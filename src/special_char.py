"""
工作上處理需要大量處理姓名中包含特殊字(難字)的問題
"""

import os
import pandas as pd

# Path
TRANSFORM_FILE_PATH = "./test.xlsx"

def main():
    
    file_name = TRANSFORM_FILE_PATH.split("/")[-1]
    
    # 檢查要處理的檔案路徑
    if os.path.exists(TRANSFORM_FILE_PATH):
        df = pd.read_excel(TRANSFORM_FILE_PATH)  # 讀取要轉換的檔案
    else:
        print("檔案路徑錯誤")
        os._exit(1)
    
    # 檢查對照表路徑
    if os.path.exists("./特殊字元轉換表.xlsx"):
        df_special_char = pd.read_excel("./特殊字元轉換表.xlsx")  # 讀取特殊字轉換表
        special_char = df_special_char[["原始字元", "轉換"]].to_dict(orient="list")
    else:
        print("'特殊字元轉換表.xlsx'不存在於資料夾中")
        os._exit(1)
    
    nums = len(special_char["原字"])
    
    # 針對不同的檔案類型(欄位)進行迴圈修改特殊字
    for i in range(nums):
        if "休學" in TRANSFORM_FILE_PATH:
            df["休學學生姓名"] = df["休學學生姓名"].str.replace(special_char["原始字元"][i], special_char["轉換"][i])
        elif "退學" in TRANSFORM_FILE_PATH:
            df["退學學生姓名"] = df["退學學生姓名"].str.replace(special_char["原始字元"][i], special_char["轉換"][i])
        else:
            df["姓名"] = df["姓名"].str.replace(special_char["原始字元"][i], special_char["轉換"][i])
    
    if os.path.exists("./output"):
        df.to_excel(f"./output/{file_name.replace('.', '_new.')}", index=False)
    else:
        os.makedirs("output")
        df.to_excel(f"./output/{file_name.replace('.', '_new.')}", index=False)
    
    print(f"{file_name.replace('.', '_new.')} had been saved to '/output'.")

if __name__ == "__main__":
    main()
