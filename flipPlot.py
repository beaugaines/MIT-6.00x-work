import random
import pylab

def flipPlot(minExp, maxExp):
    ''' assumes min and max exp pos ints; minExp < maxExp
        Plots results of 2**minExp to 2**maxExp coin flips
    '''
    ratios = []
    diffs = []
    xAxis = []

    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)

    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))

    # plot diffs

    pylab.title('Difference between heads and tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis, diffs)

    # plot ratios

    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Heads/Tails')
    pylab.plot(xAxis, ratios)


random.seed(0)
flipPlot(4, 20)
pylab.show()

