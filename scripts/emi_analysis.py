import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

def comparison(df, dept: str, score: str):
    """將2組數列進行比較(Student's t-test, Welch's t-test, Mann-Whitney U test)

    Args:
        df (pandas.DataFrame): _代入Dataset_
        dept (str): _學系代碼欄位名稱_
        score (str): _分數欄位名稱_

    Returns:
        list: _[學系名稱, 檢定方式, Statistic, P-Value, 2數列大小比較結果]_
    """
    array_a = df[(df['分組'] == 'A') & (df['學系名稱'] == dept)][score]
    array_b = df[(df['分組'] == 'B') & (df['學系名稱'] == dept)][score]

    # 先進行Normal Test，判斷數據是否為常態分布，選用Student's t-test or Welch's t-test
    k2_a, normal_test_p_value_a = stats.normaltest(array_a)
    k2_b, normal_test_p_value_b = stats.normaltest(array_b)

    # 樣本數至少須符合>=30, 且為常態分佈，則進一步進行levene檢定，確認變異數是否相等
    if len(array_a) >= 30 and len(array_b) >= 30 and normal_test_p_value_a >= 0.05 and normal_test_p_value_b >= 0.05:
        levene_statistic, levene_p_value = stats.levene(array_a, array_b)
        # levene p-value >= 0.05，則進行Student's t-test (equal_var=True)
        if levene_p_value >= 0.05:
            test_method = "Student's t-test"
            res_statistic, res_p_value = stats.ttest_ind(array_a, array_b)
        else:
            # 反之，進行Welch's t-test
            test_method = "Welch's t-test"
            res_statistic, res_p_value = stats.ttest_ind(array_a, array_b, equal_var=False)
    # 如果samples < 30，則樣本數過少，則進行Mann-Whitney U test
    else:
        test_method = "Mann-Whitney U test"
        res_statistic, res_p_value = stats.mannwhitneyu(array_a, array_b)

    # 比較2個array的mean or median
    if res_p_value <= 0.05 and test_method != "Mann-Whitney U test":
        comparison = "A > B" if array_a.mean() > array_b.mean() else "B > A"
    elif res_p_value <= 0.05 and test_method == "Mann-Whitney U test":
        comparison = "A > B" if array_a.median() > array_b.median() else "B > A"
    else:
        comparison = 'N/A'

    # 將*符號判斷加入Statistic
    if res_p_value <= 0.01:
        res_statistic = f'{res_statistic:.2f}**'
    elif 0.01 < res_p_value <= 0.05:
        res_statistic = f'{res_statistic:.2f}*'
    else:
        res_statistic = f'{res_statistic:.2f}'

    return [
        dept,
        test_method,
        res_statistic,
        f'{res_p_value:.3f}',
        comparison
    ]

def main():
    # Load Dataset
    df = pd.read_excel('./dataset.xlsx', sheet_name='df')
    # 取得"科系名稱"
    dept_list = df['學系名稱'].drop_duplicates().to_list()
    # 建立儲存List
    data_rows = []
    columns = ['學系代碼', '檢定方法', 'Statistic', 'P-Value', 'Comparison']

    for dept in dept_list:
        data_rows.append(dict(zip(columns, comparison(df, dept, 'EMI專業成績'))))

    res_df = pd.DataFrame(
        data_rows,
        columns=columns
    )
    res_df.to_csv('./result.csv', encoding='utf-8-sig', index_label='學系代碼', index=False)
    print('Done')

if __name__ == '__main__':
    main()
