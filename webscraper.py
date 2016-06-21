from bs4 import BeautifulSoup
import numpy as np
import requests
import re
import time
import random


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
        self.print_intro()

    def print_intro(self):
        print('=' * 8)
        print('Autotrader Scraping Tool - Luke Woods 2016')
        print('Vehicle: {}, {}. Searching... {} miles around {}.'
              .format(self.make, self.car_model, self.radius, self.postcode))

    def get_url(self, page_num=1):
        """Creates and returns the URL"""
        return self.url_format.format(make=self.make, car_model=self.car_model, postcode=self.postcode,
                                      radius=self.radius, page_num=page_num)

    def load_page(self, page_num=1):
        """Runs BeautifulSoup module on the results page."""
        r = requests.get(self.get_url(page_num))
        self.soup = BeautifulSoup(r.text, "html.parser")

    def get_num_pages(self):
        """Returns the number of pages of results."""
        page_res = self.soup.html.body.findAll('li', {'class': 'paginationMini__count'})
        page_text = ''.join([i.text for i in page_res])
        page_nums = (page_text.split(' ')[-1])
        return page_nums

    def get_prices(self):
        """Returns the car prices in a numpy array"""
        price_range = self.soup.html.body.findAll('div', {'class': 'search-result__price'})
        prices = np.zeros(12)
        k = 0
        for i in price_range:
            # convert string into integer
            prices[k] = int(re.sub('[^\d\.]', '', i.text[1:]))
            k += 1
        # remove first and last entries (ads)
        prices = prices[1:-1]

        print("Prices extracted ✓")
        return prices

    def get_attributes(self):
        """Returns car attributes"""
        attributes = self.soup.html.body.findAll('ul', {'class': 'search-result__attributes'})
        summary = []
        for k in range(1, 11):
            car_attr = ''
            for counter, item in enumerate(attributes[k].findAll('li')):
                if attributes[k].find(class_='js-tooltip') and counter == 0:
                    continue
                else:
                    car_attr += item.text + ' '
            summary.append(car_attr)
        return summary

    def run(self, listings, pages=3, delay=1):
        """Loops over search results and returns an array of vehicle attributes"""
        price_array = np.array([])
        attr_array = np.array([], dtype=object)
        print('='*8)
        print('BEGIN LOOP')
        for page_num in range(1, pages+1):
            print("Processing page {} of {}...".format(page_num, pages))
            listings.load_page(page_num)

            # Append attributes into array
            page_prices = listings.get_prices()
            price_array = np.append(price_array, page_prices)
            attributes = listings.get_attributes()
            attr_array = np.append(attr_array, attributes)

            # Sleep delay
            ts = time.time()
            random_sleep = delay + delay*(random.randint(0, 1000) / 1000)
            time.sleep(random_sleep)
            print('({:0.4} s delay)'.format(time.time() - ts))
        return price_array, attr_array






















