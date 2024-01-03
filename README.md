# 資料分析筆記

紀錄學習與資料分析相關的實際應用

Table of contents

- [資料分析筆記](#資料分析筆記)
  - [Data Preprocessing](#data-preprocessing)
  - [校務研究 Institutional Research](#校務研究-institutional-research)
  - [學習成效分析](#學習成效分析)
  - [相關分析](#相關分析)
    - [Pearson product-moment correlation coefficient](#pearson-product-moment-correlation-coefficient)
    - [Spearman's Rank Correlation](#spearmans-rank-correlation)

## Data Preprocessing

已完成(歸檔於`./src`):

1. [檢查特殊字元及置換](./src/special_char.py): 應用於姓名特殊字元的置換作業。

待整理(歸檔於`./test`):

1. [迴圈製作折線圖](./test/data_visualization_line_chart.py): 批量製作多個學系的折線圖。
2. [資料清理與串接](./test/data_cleasing_01.py): 將學生學籍資料、修課紀錄與成績等多個檔案進行串接與清理。

## 校務研究 Institutional Research

彙整校務研究分析上使用的方法，主要包含:

1. 學習成效分析
2. 面試/實作成績與入學後學習表現之**相關分析**

## 學習成效分析

目的: 瞭解不同組別的學生，在學習表現上是否受到具有顯著差異。

Example: 依據學生英文能力分為2組，並分析2組學生修習EMI課程是否具有顯著差異。

- 重點: 除了使用成績、平均系排名(換算PR值)等方法以外，需再加入**T-test**進行驗證。
  - Example: 分析透過不同入學管道的學生，其學習表現差異情形。

## 相關分析

目的: 為瞭解特定入學管道學生，在入學前的指定項目成績與入學後學習表現是否具有相關性，因此將進行相關分析，常用方法包含**Pearson Correlation**、**Spearman's Rank Correlation**。

### Pearson product-moment correlation coefficient

> 相關係數一般是指皮爾森積動差相關係數

- 代表兩個變數之間(X & Y)之間的線性關係。
- 分母不能為`0`，所以資料的標準差若為`0`，則不能帶入此公式。
- $p=\dfrac{x和y的變異數}{x的標準差*y的標準差}$

### Spearman's Rank Correlation

待更新。
