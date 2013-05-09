import csv

with open('nyc_addresses.csv', 'rb') as infile:
    addresses = list(csv.reader(infile))

print addresses[1]

