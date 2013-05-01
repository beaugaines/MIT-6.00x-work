import pylab

def get_data(filename):
    infile = open(filename, 'r')
    distances = []
    masses = []
    with open(filename, 'r') as infile:
        # move past header
        discard_header = infile.readline()
        for line in infile:
            d, m = line.split()
            distances.append(float(d))
            masses.append(float(m))

    return (masses, distances)

def plot_data(filename):
    xvals, yvals = get_data(filename)
    xvals = pylab.array(xvals)
    yvals = pylab.array(yvals)
    xvals = xvals * 9.81 # convert mass to force F = m*g
    pylab.plot(xvals, yvals, 'bo', label = 'Measured displacements')
    pylab.title('Measured displacements for Spring')
    pylab.xlabel('Force(Newtons)')
    pylab.ylabel('Distance(meters)')

plot_data('spring_data.txt')
pylab.show()