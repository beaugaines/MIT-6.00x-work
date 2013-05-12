import csv
import psycopg2 as psycho
import sys
import re

con = None

class CsvMunger(object):

    def __init__(self, infile):
        self.infile = infile

    def clean_address(self, address):
        lat, long = infile[]


        
# munge the file!
with open('../nyc_addresses.csv', 'rb') as infile:
    addresses = list(csv.reader(infile))

res = ()

lat, long = addresses[1][1].split()

# expunge punctuation
lat = re.sub('[(),"]', '', lat)
long = re.sub('[(),"]', '', long)

address = addresses[1][2].split()
street_num = address[0]
street = address[1] + ' ' + address[2]
city = addresses[1][5]
zip = addresses[1][6]
phone = addresses[1][7]
print addresses[1][6]




# try:
#     con = psycho.connect(database='playground', user='sircharles')
#     cur = con.cursor()

#     # create table
#     cur.execute("""

#         CREATE TABLE wifi_hotspots(id INT PRIMARY KEY,
#                                     latitude FLOAT8,
#                                     longitude FLOAT8,
#                                     zip INT,
#                                     phone INT,
#                                     free BOOL,
#                                     url varchar(256),
#                                     city varchar(20),
#                                     street varchar(30),
#                                     street_number INT,
#     """)

#     # insert records
#     query = """
#             INSERT INTO 
#                 wifi_hotspots
#                 (id, latitude, longitude, zip, phone,
#                 free, url, city, street, street_number)
#             VALUES
#                 (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#             """

#     for location in addresses:
#         cur.execute("""
#             INSERT INTO wifi_hotspots
#             VALUES 
#             """)

# except psycho.DatabaseError, e:
#     print 'Error {0}'.format(e)
#     sys.exit(1)

# finally:
#     if con:
#         con.close()


