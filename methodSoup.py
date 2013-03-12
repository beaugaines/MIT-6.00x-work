# to build up a frequency hash from a string

freq = {}

for c in string:
  freq[c] = freq.get(c, 0) + 1