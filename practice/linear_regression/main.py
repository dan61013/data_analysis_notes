"""
Reference: https://medium.com/@jason8410271027/%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-%E7%B7%9A%E6%80%A7%E5%9B%9E%E6%AD%B8-linear-regression-38b17484ee0a
Dataset source: https://www.kaggle.com/datasets/sahilislam007/sales-dataset
使用Sales Dataset進行來客數的銷售額預測
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def main():
    plt.style.use('Solarize_Light2')  # 設定Style
    df = pd.read_csv('./practice/dataset/Sales Dataset.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values(by='Date', ascending=True, inplace=True)
    df = df.groupby(by=['Date', 'Gender']).agg(
        Total_Sales=('Total Amount', 'sum'),
        Customer_Traffic=('Date', 'size')
    )

    # 使用Male資料來繪製當日來客數與銷售額的Scatter Plot
    x = df.loc[(slice(None), 'Male'), :]['Customer_Traffic'].values.reshape(-1, 1)
    y = df.loc[(slice(None), 'Male'), :]['Total_Sales'].values.reshape(-1, 1)
    model = LinearRegression()
    regressor = model.fit(x, y)
    print(f'Intercept: {regressor.intercept_}')  # 取得截距
    print(f'Slop: {regressor.coef_}')  # 取得斜率
    print(regressor.predict([[7]]))  # 取得某一個數值的預測值，以這個case而言，就是取得customer traffic=4的銷售額

    plt.scatter(
        df.loc[(slice(None), 'Male'), :]['Customer_Traffic'],
        df.loc[(slice(None), 'Male'), :]['Total_Sales'],
        color='#75eb9c'
    )

    plt.plot(
        df.loc[(slice(None), 'Male'), :]['Customer_Traffic'].drop_duplicates().sort_values().to_list(),
        [regressor.predict([i])[0] for i in np.reshape(df.loc[(slice(None), 'Male'), :]['Customer_Traffic'].drop_duplicates().sort_values().to_list(), (-1, 1))],
        color='#294e9e'
    )

    plt.title('Sales By Customer Traffic')
    plt.xlabel('Customer Traffic')
    plt.ylabel('Total Sales')
    plt.tight_layout()
    plt.savefig('./practice/linear_regression/plot.png')
    plt.show()

if __name__ == '__main__':
    main()
