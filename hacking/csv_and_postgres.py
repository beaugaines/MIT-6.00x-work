import csv
import psycopg2 as psycho
import sys

DB = 'nyc-wifi.db'
con = None

# munge the file!
with open('../nyc_addresses.csv', 'rb') as infile:
    addresses = list(csv.reader(infile))

print addresses[1]

try:
    con = psycho.connect(database='playground', user='sircharles')
    cur = con.cursor()

    # create table
    cur.execute("""

        CREATE TABLE wifi_hotspots(id INT PRIMARY KEY,
                                    latitude FLOAT8,
                                    longitude FLOAT8,
                                    zip INT,
                                    phone INT,
                                    free BOOL,
                                    url varchar(256)

    """)

except psycho.DatabaseError, e:
    print 'Error {0}'.format(e)
    sys.exit(1)

finally:
    if con:
        con.close()


