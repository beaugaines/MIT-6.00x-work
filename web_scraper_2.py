from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

BASE_URL = ("http://chicagomag.com/Chicago-Magazine/"
            "November-2012/Best-Sandwiches-Chicago/")


word_soup = BeautifulSoup(urlopen(BASE_URL).read())

sammies = word_soup.find_all('div', 'sammy')

sammy_urls = [div.a['href'] for div in sammies]



