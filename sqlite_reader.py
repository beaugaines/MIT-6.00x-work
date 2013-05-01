import sqlite3 as lite
import sys

DB = 'best-of.db'
con = lite.connect(DB)

with con:
    cur = con.cursor()
    cur.execute('SELECT * from bestof')

    # rows = cur.fetchall()

    # for row in rows:
    #     print row