from Webscraper import TradeList

listings = TradeList('toyota', 'yaris', 'ox12jd', '100')
listings.load_page(page_num=1)

url = listings.get_url()
print(url)

num_pages = listings.get_num_pages()
print(num_pages)

prices = listings.get_prices()
print(prices)