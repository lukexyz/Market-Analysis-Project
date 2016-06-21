import numpy as np
import pandas as pd


class DataCleaner(object):
    def __init__(self, prices, attributes, url_ids, urls):
        self.prices = prices
        self.attributes = attributes
        self.url_ids = url_ids
        self.urls = urls

    def get_df(self):
        prices = self.prices
        attr = self.attributes
        ids = self.url_ids
        urls = self.urls
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
                'Miles': miles,
                'ID': ids,
                'Url': urls}
        df = pd.DataFrame(data, columns=['Price', 'Year', 'Miles', 'ID', 'Url'])

        return df



