import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class MarketValue(object):
    def __init__(self, df):
        print('Graphing Market Analysis...')

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
