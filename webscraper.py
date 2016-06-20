from bs4 import BeautifulSoup
import pandas as pd
import requests
import re


class TradeList(object):
    """
    A web scraper to extract sales attributes on autotrader.co.uk
    Specify the make, model, postcode and search radius for the vehicle

    Part of a larger machine learning sales analytics project.
    """
    def __init__(self, make, car_model, postcode, radius):
        self.make = make
        self.car_model = car_model
        self.postcode = postcode
        self.radius = radius
        self.url_format = "http://www.autotrader.co.uk/search/used/cars/{make}/{car_model}/" \
                          "postcode/{postcode}/radius/{radius}/searchcontext/default/sort/" \
                          "priceasc/onesearchad/new%2Cnearlynew%2Cused/page/{page_num}"
        self.soup = None

    def get_url(self, page_num=1):
        """Creates and returns the URL"""
        return self.url_format.format(make=self.make, car_model=self.car_model, postcode=self.postcode,
                                      radius=self.radius, page_num=page_num)

    def load_page(self, page_num=1):
        """Runs BeautifulSoup module on the results page."""
        r = requests.get(self.get_url(page_num))
        self.soup = BeautifulSoup(r.text, "html.parser")
        print("BeautifulSoup: page loaded successfully ✓")

    def get_num_pages(self):
        """Returns the number of pages of results."""
        page_res = self.soup.html.body.findAll('li', {'class': 'paginationMini__count'})
        page_text = ''.join([i.text for i in page_res])
        page_nums = (page_text.split(' ')[-1])
        return page_nums

    def get_prices(self):
        """Returns the car prices in a Pandas series"""
        price_range = self.soup.html.body.findAll('div', {'class': 'search-result__price'})
        prices = pd.Series([])
        k = 0
        for i in price_range:
            # convert string into integer
            prices[k] = int(re.sub("[^\d\.]", "", i.text[1:]))
            k += 1
        # remove first and last entries (ads)
        prices = prices[1:-1]

        print("Prices extracted ✓")
        return prices
























