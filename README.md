# Market Analysis with Machine Learning

A web scraper that downloads vehicle attributes from Autotrader.co.uk and graphs the results.

Machine learning algorithms are applied to approximate market value, and the listings which 
deviate the most from market value are returned.

#### Usage
```
# Web scraper instance
listings = TradeList('Toyota', 'Yaris', 'OX12JD', '50')

# Run
listings.run(listings, pages=100, delay=2)
```


<img src=https://raw.githubusercontent.com/lukexyz/Market-Analysis-Project/master/img/plots-toyotayaris.png>

