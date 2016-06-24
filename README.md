# Market Analysis with Machine Learning

A web scraper that downloads vehicle attributes from Autotrader.co.uk and graphs the results.

Machine learning algorithms are applied to approximate market value, and the listings which 
deviate the most from market value are returned.


#### Usage
<img align="right" src="https://raw.githubusercontent.com/lukexyz/Market-Analysis-Project/master/img/search-pagesmall.png">

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

##### Market Suggestions

The output data frame lists the results by deviation from market. The market price was approximated 
using the sklearn linear regression model.

The vehicle unique ID and url are included in the extended data frame.

```
Graphing Market Analysis...

Train/test:  744 249
Predictions: [ 3781.47831641  2976.49471733  2095.35390833  2559.1202901   3815.79622688] 
Actual Price: [ 3395.  2650.  2895.  1900.  3395.]
LR Score : 0.76235
Coefficients: [[  289.900502  -0.01143930]]

      Price   Pred_price  Price_difference    Year    Miles  Category  
129   995.0  2263.339986          -1268.34  2005.0  74000.0       0.0   
215  1395.0  2549.322574          -1154.32  2005.0  49000.0       0.0   
302  1795.0  2880.232885          -1085.23  2008.0  96100.0       0.0   
297  1790.0  2862.101682          -1072.10  2006.0  47000.0       0.0   
154   995.0  2057.432523          -1062.43  2005.0  92000.0       0.0   
153   995.0  2057.432523          -1062.43  2005.0  92000.0       0.0   
133   995.0  2052.908326          -1057.91  2004.0  67053.0       0.0   
56    750.0  1792.212366          -1042.21  2003.0  64500.0       0.0   
493  2495.0  3525.895725          -1030.90  2009.0  65000.0       0.0   
434  2299.0  3323.591737          -1024.59  2007.0  32000.0       0.0  
```