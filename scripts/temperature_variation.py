"""
用途: 將測試數據製作成溫度-時間折線圖。
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def main():

    # set the basic variable
    CSV_PATH = "./docs/row_data"
    TITLE_NAMED_LIST = ["0%", "50%", "100%", "Stopped"]
    TEST_ORDER_LIST = ["First", "Second", "Third"]

    # Loading the csv files
    csv_file_list = os.listdir(CSV_PATH)

    # Read CSV files to List
    df_list = [pd.read_csv(f"{CSV_PATH}/{file}", encoding="ISO-8859-1") for file in csv_file_list]

    # Set the figure 2x2
    fig, ax = plt.subplots(2, 2, figsize=(16, 9))
    axes = ax.flatten()

    for i, title_name in enumerate(TITLE_NAMED_LIST):
        sub_ax = axes[i]
        for j, test_order in enumerate(TEST_ORDER_LIST):
            idx = i * len(TEST_ORDER_LIST) + j
            df = df_list[idx]
            df = df.iloc[:-2]
            drive_temp = [col for col in df.columns if 'Drive' in col][0]
            df.loc[:, drive_temp] = df[drive_temp].astype(float)
            sub_ax.plot(df["Time"],
                        df[drive_temp],
                        marker='o',
                        markersize=2,
                        label=test_order)

        sub_ax.set_title(f"The M.2 SSD temperature when fan efficiency is {title_name}")
        sub_ax.legend(
            loc="upper right",
            shadow=True
        )
        # Hide the X axis values
        sub_ax.set_xticks([])
        sub_ax.set_xlabel("Time", labelpad=6.0)
        sub_ax.set_ylabel("Drive Temperature", labelpad=6.0)
        sub_ax.set_ylim(45, 65)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
