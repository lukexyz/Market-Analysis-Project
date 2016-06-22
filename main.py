from webscraper import TradeList
from datacleaner import DataCleaner


listings = TradeList('Toyota', 'Yaris', 'OX12JD', '100')

# Initiate loop
price_array, attributes, url_ids, urls = listings.run(listings, pages=10, start_page=1, delay=1)

# print('hi')
# print(listings.get_prices())
# listings.get_attributes()

# Output
print('='*8)
print('PRICE DATA')
print(price_array[:10])
print('                                        →(Viewing 10 of {})'.format(len(price_array)))
print('')
print('ATTRIBUTES')
print(attributes[:4])
print('                                        →(Viewing 4 of {})'.format(len(attributes)))
print('')
print('='*8)

# Cleaning data

print('array sizes {} {} {} {}'.format(len(price_array), len(attributes), len(url_ids), len(urls)))

# clean = DataCleaner(price_array, attributes, url_ids, urls)
#
# df = clean.get_df()
# print(df.iloc[:5, :-1])    # 5 rows, remove url column
#
#
# df.to_csv('yaris50-100.csv')