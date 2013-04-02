import pylab


""" simple fcn to parse a text file of temperature data and print out
    the daily high-low differential using pyplot
"""

# initialize our storage
highs = []
lows = []


#read in the file, split the lines, and push the relevant data onto the high/low arrays

with open('julyTemps.txt') as f:
    for line in f.readlines():
        fields = line.split()
        if len(fields) < 3 or not fields[0].isdigit():
            pass
        else:
            highs.append(int(fields[1]))
            lows.append(int(fields[2]))


# calculate daily temp differentials

diffTemps = []
for i in range(len(highs)):
    diffTemps.append(highs[i] - lows[i])


# plot it
pylab.plot(range(1,32), diffTemps)
pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
pylab.xlabel('Days')
pylab.ylabel('Temperature Ranges')
pylab.show()




