from webscraper import TradeList
from datacleaner import DataCleaner

# Web scraper instance
listings = TradeList('Toyota', 'Yaris', 'OX12JD', '100')

# Initiate loop
price_array, attributes, url_ids, urls = listings.run(listings, pages=100, start_page=1, delay=2)

# Format output
print('='*8)
print('PRICE DATA')
print(price_array[:10])
print('                                        →(Viewing 10 of {})'.format(len(price_array)))
print('')
print('ATTRIBUTES')
print(attributes[:4])
print('                                        →(Viewing 4 of {})'.format(len(attributes)))
print('='*8)
print('Array sizes {} {} {} {}'.format(len(price_array), len(attributes), len(url_ids), len(urls)))
print('')

# Cleaning data
clean = DataCleaner(price_array, attributes, url_ids, urls)

# Display data frame
df = clean.get_df()
print(df.iloc[:5, :-1])    # 5 rows, remove url column

# Save results
df.to_csv('yaris{}.csv'.format(len(df)))