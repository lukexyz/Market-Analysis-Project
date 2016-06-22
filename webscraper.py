from bs4 import BeautifulSoup
import numpy as np
import requests
import re
import time
import random


class TradeList(object):
    """
    A web scraper to extract sales attributes from autotrader.co.uk
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

    def get_url_ids(self):
        """Return unique url ID."""
        links = self.soup.html.body.findAll('a', {'class': 'gui-test-search-result-link'})
        url_id = [''] * 10
        k = 0
        for link in links:
            url_id[k] = str(re.findall('\d+', link.get('href'))[0])
            k += 1
        return url_id

    def get_urls(self):
        """Return the url."""
        links = self.soup.html.body.findAll('a', {'class': 'gui-test-search-result-link'})
        url = [''] * 10
        k = 0
        for link in links:
            url[k] = link.get('href')
            k += 1
        return url

    def run(self, listings, pages=3, start_page=1, delay=1):
        """Loops over search results and returns an array of vehicle attributes"""
        price_array = np.array([])
        attr_array = np.array([], dtype=object)
        url_id_array = np.array([])
        url_array = np.array([])

        print('='*8)
        print('BEGIN LOOP')
        for page_num in range(start_page, start_page + pages):
            listings.load_page(page_num)
            print('HI')
            print(listings.get_url(page_num))

            if page_num == start_page:
                print(" → of {} total pages".format(listings.get_num_pages()))
                print('')
            print("Processing page {} of {}...".format(page_num, pages))

            try:
                # Append attributes into array
                price_array = np.append(price_array, listings.get_prices())
                attr_array = np.append(attr_array, listings.get_attributes())
                url_id_array = np.append(url_id_array, listings.get_url_ids())
                url_array = np.append(url_array, listings.get_urls())

            except Exception as e:
                print('An error occurred on page {}: {}'.format(page_num, e))
                print(len(price_array), len(attr_array), len(url_id_array), len(url_array))

            # Sleep delay
            ts = time.time()
            random_sleep = delay + delay*(random.randint(0, 1000) / 1000)
            time.sleep(random_sleep)
            print('({:0.4} s delay)'.format(time.time() - ts))

        return price_array, attr_array, url_id_array, url_array
