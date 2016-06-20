from webscraper import TradeList

listings = TradeList('toyota', 'yaris', 'ox12jd', '100')
listings.load_page(page_num=1)

url = listings.get_url()
print(url)
num_pages = listings.get_num_pages()
print(num_pages)
prices = listings.get_prices()
print(prices)


# Start loop

price_array, attributes = listings.run(listings, pages=2, delay=1)

print('='*8)
print('DATA')
print(price_array)
print('')

# attributes = listings.get_attributes()
print(attributes)