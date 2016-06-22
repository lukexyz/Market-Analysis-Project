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

<img src=https://i.imgur.com/0wifowN.gif>

<p>
The Boids simulation follows three core rules:


* Separation: steer to avoid crowding local flockmates
* Alignment: steer towards the average heading of local flockmates
* Cohesion: steer to move toward the average position (center of mass) of local flockmates
