# 資料分析筆記(2023)

紀錄今年學習與資料分析相關的實際應用

Table of contents

- [資料分析筆記(2023)](#資料分析筆記2023)
  - [Data Preprocessing](#data-preprocessing)
  - [相關分析](#相關分析)
    - [Pearson product-moment correlation coefficient](#pearson-product-moment-correlation-coefficient)
    - [Spearman's Rank Correlation](#spearmans-rank-correlation)

## Data Preprocessing

1. [檢查特殊字元及置換](./src/special_char.py)
2. [迴圈製作折線圖](./test/data_visualization_line_chart.py)
3. [資料清理與串接](./test/data_cleasing_01.py)

## 相關分析

目前在校務研究中，最常使用的是**Pearson Correlation**, **Spearman's Rank Correlation**

### Pearson product-moment correlation coefficient

> 相關係數一般是指皮爾森積動差相關係數

- 代表兩個變數之間(X & Y)之間的線性關係。
- 分母不能為`0`，所以資料的標準差若為`0`，則不能帶入此公式。
- $p=\dfrac{x和y的變異數}{x的標準差*y的標準差}$

### Spearman's Rank Correlation

待更新。
