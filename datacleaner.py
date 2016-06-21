import numpy as np
import pandas as pd


class DataCleaner(object):
    def __init__(self, prices, attributes):
        self.prices = prices
        self.attributes = attributes
        print('done')

    def get_df(self):
        prices = self.prices
        attr = self.attributes
        print('Returning Pandas DF')

        # Extracting values from string
        years = np.zeros(len(attr))
        miles = np.zeros(len(attr))
        for i in range(len(attr)):
            # Example string:
            # '2000 (W reg) Hatchback 177,000 miles Manual 1.0L 67 bhp Petrol '
            years[i] = int(attr[i].split(' ')[0])
            miles[i] = int(attr[i].split(' ')[4].replace(",", ""))

        # Create data frame
        data = {'Price': prices,
                'Year': years,
                'Miles': miles}
        df = pd.DataFrame(data, columns=['Price', 'Year', 'Miles'])

        return df



