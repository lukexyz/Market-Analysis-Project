import numpy as np


class DataCleaner(object):
    def __init__(self, prices, attributes):
        self.prices = prices
        self.attributes = attributes
        print('done')

    def get_df(self):
        prices = self.prices
        attr = self.attributes
        print('Returning Pandas DF')

        return years

    # def get_years(self, attr):
    #     """Returns the cleaned year attribute"""
    #     years = np.zeros(len(attr))
    #     for i in range(len(attr)):
    #         years[i] = int(attr[i].split(' ')[0])
    #     return years
    #
    # def get_miles(self, attr):
    #     """Returns the cleaned miles attribute"""
    #     miles = np.zeros(len(attr))
    #     for i in range(len(attr)):
    #         years[i] = int(attr[i].split(' ')[0])
    #     return miles


