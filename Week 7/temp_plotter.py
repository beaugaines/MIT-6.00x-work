
""" simple fcn to parse a text file of temperature data and print out
    the daily high-low differential using pyplot
"""

# initialize our storage
highs = []
lows = []

allTemps = []

#read in the file
with open('julyTemps.txt') as f:
  for line in f.readlines():
    if len(line) < 3 or not line[0].isdigit():
      pass
    else:
      allTemps.append(line.split())


# inFile = open('julyTemps.txt')

# for line in inFile:
#   fields = line.split()
#   if len(fields) < 3 or not fields[0].isdigit():
#     pass
#   else:
#     allTemps.append(fields)

for f in allTemps:
  print f

# for f in fields:
#   if len(f) < 3 or not f[0].isdigit() or f[0] == '-':
#     fields.remove(f)
#   else:
#     continue


# for f in fields:
#   print f


# for field in fields:
#   if len(field) < 3 or not field[0].isdigit():
#     fields.remove(field)


# for f in fields:
#   print f