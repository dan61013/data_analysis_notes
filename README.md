# Data Analysis Notes

Link:

- [Supported TeX/LaTeX commands](https://docs.mathjax.org/en/latest/input/tex/macros/index.html)

Table of contents:

- [Data Analysis Notes](#data-analysis-notes)
  - [Data Preprocessing](#data-preprocessing)
    - [Data Preprocessing Scripts](#data-preprocessing-scripts)
  - [校務研究 Institutional Research](#校務研究-institutional-research)
  - [學習成效分析](#學習成效分析)
  - [相關分析](#相關分析)
    - [Pearson product-moment correlation coefficient](#pearson-product-moment-correlation-coefficient)
  - [Linear Regression](#linear-regression)
  - [平均絕對偏差](#平均絕對偏差)
  - [Others](#others)
    - [Git LFS (Large File Storage)](#git-lfs-large-file-storage)

## Data Preprocessing

> Data Preprocessing是指將row data轉換成對於分析或模型訓練更適合的格式。

### Data Preprocessing Scripts

1. [檢查特殊字元及置換](./scripts/special_char.py): 應用於姓名特殊字元的置換作業。
2. [迴圈製作折線圖](./scripts/data_visualization_line_chart.py): 批量製作多個學系的折線圖。
3. [資料清理與串接](./scripts/data_cleasing_01.py): 將學生學籍資料、修課紀錄與成績等多個檔案進行串接與清理。
4. [製作多組測試數據的(溫度-時間)折線圖](./scripts/temperature_variation.py): 將[HWiNFO](https://www.hwinfo.com/) Output數據製作成折線圖。

## 校務研究 Institutional Research

在校務研究中所分析的議題主要包含:

1. 學習成效分析
2. 面試/實作成績與入學後學習表現之**相關分析**

## 學習成效分析

目的: 瞭解不同組別的學生，在特定的課程中，其學習表現是否具有顯著差異。

Example: 依據學生英文能力，將每一個學系的學生分為2組，並分析2組學生修讀EMI(全英文授課)之課程是否具有顯著差異。

分析方法: 原先採用**Student's t-test**進行分析，但由於各學系的samples低於30，因此改為依照下列條件進行對應的分析:

1. 當samples >= 30、為常態分布(D'Agostino-Pearson檢驗)，以及levene檢驗之**P-Value >= 0.05**，才進行**Student's t-tes**(`equal_var=True`)。
2. 當samples >= 30、為常態分布(D'Agostino-Pearson檢驗)，但levene檢驗之**P-Value < 0.05**，則進行**Welch's t-test**(`equal_var=False`)。
3. 當samples <= 30，則採用**Mann-Whitney U test**。

分析結果(範例)如下，或參考這份[CSV output file](./scripts/output/result.csv)，點擊[這裡](./scripts/emi_analysis.py)查看Script(不包含data preprocessing):

| 學系代碼 | 檢定方法          | Statistic | P-Value | Comparison |
| :------: | :---------------: | :-------: | :-----: | :--------: |
|   A001   | Student's t-test  |   -1.04   |  0.301  |    N/A     |
|   A002   | Mann-Whitney U test |  1286.00  |  0.956  |    N/A     |
|   A003   | Mann-Whitney U test | 1987.00\* |  0.027  |   B > A    |
|   A004   | Mann-Whitney U test |  2395.50  |  0.864  |    N/A     |
|   A005   | Mann-Whitney U test |  2890.00  |  0.164  |    N/A     |
|   A006   | Mann-Whitney U test |   123.00  |  0.209  |    N/A     |
|   A007   | Mann-Whitney U test |   351.50  |  0.440  |    N/A     |
|   A008   | Mann-Whitney U test | 681.50\* |  0.015  |   B > A    |
|   A009   | Mann-Whitney U test | 150.00\*\*|  0.001  |   B > A    |
|   A010   | Mann-Whitney U test |   37.50   |  0.788  |    N/A     |
|   A011   | Mann-Whitney U test |   359.50  |  0.149  |    N/A     |
|   A012   | Mann-Whitney U test | 296.50\*\*|  0.003  |   B > A    |

- 英文能力定義: B > A 組
- N/A: 代表P-Value不具有顯著性，因此沒有將兩組學生進行比較。

## 相關分析

目的: 為瞭解特定入學管道學生，在入學前的指定項目成績與入學後學習表現是否具有相關性，因此將進行相關分析，常用方法包含**Pearson Correlation**、**Spearman's Rank Correlation**。

### Pearson product-moment correlation coefficient

> 相關係數一般是指皮爾森積動差相關係數

- 代表兩個變數之間(X & Y)之間的線性關係。
- 分母不能為`0`，所以資料的標準差若為`0`，則不能帶入此公式。
- $p=\dfrac{x和y的變異數}{x的標準差*y的標準差}$

## Linear Regression

| Refernce: [學習筆記-線性回歸(Linear Regression)](https://medium.com/@jason8410271027/%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E7%B7%9A%E6%80%A7%E5%9B%9E%E6%AD%B8-linear-regression-38b17484ee0a)

主要公式: $y=\beta_0+\beta_1x$

自我練習: [實作Scatter & 繪製預測線](./practice/linear_regression/main.py)

![Sales By Customer Traffic](./practice/linear_regression/plot.png)

## 平均絕對偏差

> Mean Absolute Deviation (MAD, AAD -> AverageAD): 用於表示各變量之間的離散程度，可以使用Mean, Median or Mode三種方式。

實作 -> [Jupyter Notebook](./tutorial/Pandas/pd_modifying_data.ipynb):

- Dummy Data -> [學生修課資料與成績](./tutorial/dataset/學生修課資料與成績.csv)，分析每一筆資料的Absolute Deviation，並計算MAD

※ 位於`In [29]`~

Result:

Mean Absolute Deviation: `22.779`

超過MAD的紀錄:

|   學年度 |   學期 | 學號   | 就讀班級   | 課程代碼   |   成績 | 年級   |   Absolute Deviation |
|---------:|-------:|:-------|:-----------|:-----------|-------:|:-------|---------------------:|
|      110 |      1 | A2372  | 資訊一甲   | R53862     |     90 | 大一   |                36.81 |
|      110 |      1 | A8406  | 材料二甲   | R45288     |      6 | 大二   |                47.19 |
|      110 |      1 | A2950  | 資訊一乙   | R31748     |     16 | 大一   |                37.19 |
|      110 |      1 | A5486  | 資訊一乙   | R45902     |     25 | 大一   |                28.19 |
|      110 |      1 | A6658  | 資訊一乙   | R38323     |      8 | 大一   |                45.19 |
|      110 |      1 | A7583  | 化學三甲   | R37639     |     77 | 大三   |                23.81 |
|      110 |      1 | A4190  | 資訊二甲   | R45944     |     83 | 大二   |                29.81 |
|      110 |      1 | A5175  | 資訊二甲   | R40624     |     83 | 大二   |                29.81 |
|      110 |      1 | A8857  | 資訊二甲   | R31315     |     76 | 大二   |                22.81 |
|      110 |      1 | A8394  | 化學三甲   | R20756     |     23 | 大三   |                30.19 |
|      110 |      1 | A7377  | 材料二甲   | R55532     |     77 | 大二   |                23.81 |
|      110 |      1 | A1607  | 資訊一乙   | R94199     |     80 | 大一   |                26.81 |
|      110 |      1 | A5407  | 材料二甲   | R40596     |     19 | 大二   |                34.19 |
|      110 |      1 | A4452  | 材料二甲   | R93028     |     96 | 大二   |                42.81 |
|      110 |      1 | A5215  | 資訊一乙   | R51908     |     19 | 大一   |                34.19 |

## Others

### Git LFS (Large File Storage)

> 為了解決大檔案無法存放在GitHub上，需存放在LFS儲存空間。

Step:

1. 安裝[Git LFS](https://git-lfs.com/)
2. 在Project路徑下輸入: `git lfs install`
3. 指定檔案: `git lfs track "file_path"`，或指定所有類型檔案`git lfs track "*.csv"`
4. 上述指令會新增一個`.gitattributes`檔案，要add這個檔案`git add .gitattributes`
5. 進行commit與push
6. Done.
