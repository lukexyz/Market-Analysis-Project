from webscraper import TradeList
from datacleaner import DataCleaner


listings = TradeList('Toyota', 'Yaris', 'OX12JD', '100')

# Initiate loop
price_array, attributes, url_ids, urls = listings.run(listings, pages=1, delay=0)

# Output
print('='*8)
print('PRICE DATA')
print(price_array[:10])
print('                                        →(Viewing 10 of {})'.format(len(price_array)))
print('')
print('ATTRIBUTES')
print(attributes[:4])
print('                                        →(Viewing 4 of {})'.format(len(attributes)))
print('='*8)

# Cleaning data
clean = DataCleaner(price_array, attributes, url_ids, urls)
df = clean.get_df()
print(df.iloc[:, :-1])    # remove url column
