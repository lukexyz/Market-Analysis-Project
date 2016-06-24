# Market Analysis with Machine Learning

A web scraper that downloads vehicle attributes from Autotrader.co.uk and graphs the results.

Machine learning algorithms are applied to approximate market value, and the listings which 
deviate the most from market value are returned.


#### Usage
<img style=float:right src=https://raw.githubusercontent.com/lukexyz/Market-Analysis-Project/master/img/search-pagesmall.png>

##### Run web scraper


```
from webscraper import TradeList

listings = TradeList('Toyota', 'Yaris', 'OX12JD', '50')
listings.run(listings, pages=100, delay=2)
```

##### Clean data
```
from datacleaner import DataCleaner

df = DataCleaner(price_array, attributes, url_ids, urls, category)
df = clean.get_df()
```

##### Analyse results
```
from analysis import MarketValue
MarketValue(df)
```

<img src=https://raw.githubusercontent.com/lukexyz/Market-Analysis-Project/master/img/plots-toyotayaris.png>

