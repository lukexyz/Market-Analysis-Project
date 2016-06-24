import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split

class MarketValue(object):
    def __init__(self, df):
        print('Graphing Market Analysis...')

        # Create ML model
        data = df.iloc[:, 1:3].as_matrix()
        target = df.iloc[:, :1].as_matrix()

        X_train, X_test, y_train, y_test = train_test_split(data, target)
        print('')
        print('Train/test: ', len(X_train), len(X_test))

        model_lr = LinearRegression()
        model_lr.fit(X_train, y_train)

        model_lr.score(X_test, y_test)

        pred = model_lr.predict(X_test)
        print('Predictions: {} '.format(np.hstack(pred[:5])))
        print('Actual Price: {}'.format(np.hstack(y_test[:5])))
        print('Coefficients: {}'.format(model_lr.coef_))
        print('')

        market = model_lr.predict(data)
        df.insert(1, "Pred_price", market)
        diff = round(df['Price'] - df['Pred_price'], 2)
        df.insert(2, "Price_difference", diff)
        print(df[df.Category == 0].sort_values('Price_difference').head(10))


        # Plot: Price by miles
        sns.jointplot(df.Miles, df.Price, kind="reg")
        plt.ylim(0, 5000)
        plt.xlim(0, 250000)

        # Plot: Price by age
        sns.jointplot(df.Year, df.Price, kind="reg", x_jitter=.5)
        plt.ylim(0, 5000)
        plt.xlim(1995, 2016)
        plt.show()

if __name__ == '__main__':
    df1 = pd.read_csv('yaris993.csv', index_col=0)
    MarketValue(df1)
