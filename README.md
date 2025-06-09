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

目的: 瞭解不同組別的學生，在學習表現上是否受到具有顯著差異。

Example: 依據學生英文能力分為2組，並分析2組學生修讀EMI課程是否具有顯著差異。

- 重點: 除了使用成績、平均系排名(換算PR值)等方法以外，需再加入**T-test**進行驗證。
  - Example: 分析透過**不同入學管道**入學的學生，其學習表現差異情形。

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

自我練習: [實作Scatter & 繪製預測線]('./practice/linear_regression/main.py')

![Sales By Customer Traffic](./practice/linear_regression/plot.png)
