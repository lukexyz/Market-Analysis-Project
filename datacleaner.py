import numpy as np
import pandas as pd


class DataCleaner(object):
    def __init__(self, prices, attributes, url_ids, urls, category):
        self.prices = prices
        self.attributes = attributes
        self.url_ids = url_ids
        self.urls = urls
        self.category = category

    def get_df(self):
        """
        Returns pandas dataframe with vehicle data
        """
        prices = self.prices
        attr = self.attributes
        ids = self.url_ids
        urls = self.urls
        category = self.category

        print('Returning Pandas DF')

        # Extracting values from string
        years = np.zeros(len(attr))
        miles = np.zeros(len(attr))

        for i in range(len(attr)):
            # Example string:
            # '2000 (W reg) Hatchback 177,000 miles Manual 1.0L 67 bhp Petrol '
            try:
                if len(attr[i].split(' ')) == 12:
                    years[i] = int(attr[i].split(' ')[0])
                    miles[i] = int(attr[i].split(' ')[4].replace(",", ""))
                else:
                    # Row elements -1 if data is invalid
                    years[i] = -1
                    miles[i] = -1
            except Exception as e:
                print('Error: {}'.format(e))
                print('On string: {}'.format(attr[i]))
                years[i] = -1
                miles[i] = -1

        # Create data frame
        data = {'Price': prices,
                'Year': years,
                'Miles': miles,
                'Category': category,
                'ID': ids,
                'Url': urls}
        df = pd.DataFrame(data, columns=['Price', 'Year', 'Miles', 'Category', 'ID', 'Url'])

        # Drop invalid data
        df = df.loc[df.Year > 0]

        print('Shape: {}'.format(df.shape))
        return df



