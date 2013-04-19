from bs4 import BeautifulSoup
from urllib2 import urlopen

BASE_URL = "http://www.chicagoreader.com"

def get_category_links(section_url):
    html = urlopen(section_url).read()
    # maybe use HTML5 parser instead?
    soup = BeautifulSoup(html, 'lxml')
    boccat = soup.find('dl', 'boccat')
    category_links = [BASE_URL + dd.a['href'] for dd in boccat.findAll('dd')]
    return category_links

def get_category_winner(category_url):
    html = urlopen(category_url).read()
        