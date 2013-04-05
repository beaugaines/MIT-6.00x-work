class Location(object):


    def __init__(self):
        """x and y are floats"""
        self.x = x
        self.y = y


    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y)



class Field(object):

    def __init__(self):
        self.drunks = {}

        def addDrunk(self, drunk, loc):
            # add a new drunk to the field at location loc
            if drunk in self.drunks:
                raise ValueError('Duplicate drunk')
            else:
                self.drunks[drunk] = loc

        def moveDrunk(self, drunk):
            if not drunk in self.drunks:
                raise ValueError("Drunk not in field")
            xDist, yDist = drunk.takeStep()
            currentLocation = self.drunks[drunk]
            # use move method of Location class to get new location
            self.drunks[drunk] = currentLocation.move(xDist, yDist)

        def getLoc(self, drunk):
            if not drunk in self.drunks:
                raise ValueError("Drunk not in field")
            return self.drunks[drunk]

class Drunk(object):

    def __init__(self):
        self.name = name

    def __str__(self):
        return 'This drunk is named ' + self.name

class UsualDrunk(Drunk):
    """not to be confused with the unusual drunk"""
    def takeStep(self):
        stepChoices = \
        [(0.0, 1.0), (0.0, -1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


def walk(f, d, numSteps):
    # use Field's getLoc fcn to determine drunk's location
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(start.distFrom(f.getLoc(d)))

def simWalks(numSteps, numTrials):
    homer = UsualDrunk('Homer')
    origin = Location(0,0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walk(f, homer, numSteps))
    return distances

def drunkTest(numTrials = 20):
    for numSteps in [10, 100, 1000, 10000]:
        distances = simWalks(numSteps, numTrials)
        print 'Random walk of ' + str(numSteps)
        print 'Mean = ', sum(distances)/len(distances)
        print 'Max = ', max(distances) + ", Min = ", min(distances) 


drunkTest()