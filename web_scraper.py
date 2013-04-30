from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep
import sqlite3 as lite

BASE_URL = "http://www.chicagoreader.com"
DB = 'best-of.db'

# connect to sqlite

con = None

# try:
#     con = lite.connect(DB)
#     cur = con.cursor()
#     cur.execute('SELECT SQLITE_VERSION()')

#     data = cur.fetchone()

#     print "SQLite version: {0}".format(data)
# except lite.Error, e:
#     print "Error {0}".format(e.args[0])
#     sys.exit(1)
# finally:
#     if con:
#         con.close()

# more compact version using 'with' - which automatically
# releases the resources and handles errors too

con = lite.connect(DB)

with con:
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()

    print "SQLite version: {0}".format(data)


def make_soup(url):
   html = urlopen(url).read()
   # maybe use HTML5 parser instead?
   return BeautifulSoup(html, 'lxml')

def get_category_links(section_url):
    soup = make_soup(section_url)
    boccat = soup.find('dl', 'boccat')
    category_links = [BASE_URL + dd.a['href'] for dd in boccat.findAll('dd')]
    print 'success'
    return category_links

def get_category_winner(category_url):
    soup = make_soup(category_url)
    print 'soup!'
    category = soup.find('h1', 'headline').string
    winner = [h2.string for h2 in soup.findAll('h2', 'boc1')]
    runners_up = [h2.string for h2 in soup.findAll('h2', 'boc2')]
    return {'category': category,
            'category_url': category_url,
            'winner': winner,
            'runners_up': runners_up
            }
       
if __name__ == '__main__':
    food_and_drink = ('http://www.chicagoreader.com/chicago/'
                        'best-of-chicago-2011-food-drink/BestOf?oid=4106228')

    categories = get_category_links(food_and_drink)

    limit = 0
    data = []
    for category in categories:
        winner = get_category_winner(category)
        data.append(winner)
        limit += 1
        if limit == 5:
            break
        sleep(1) # be kind to chicago reader site!

    print data