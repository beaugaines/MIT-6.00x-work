
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
    fields = line.split()
    if len(fields) < 3 or not fields[0].isdigit():
      pass
    else:
      highs.append(fields[1])
      lows.append(fields[2])



