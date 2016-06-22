import pandas as pd
import seaborn as sns


class MarketValue(object):
    def __init__(self, df):
        print('market analysis complete :)')
        sns.jointplot(df.Year, df.Price, kind="reg")