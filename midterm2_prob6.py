import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    global CURRENTRABBITPOP
    global MAXRABBITPOP

    if CURRENTRABBITPOP < MAXRABBITPOP:
        if random.random() <= (1.0 - float(CURRENTRABBITPOP)/MAXRABBITPOP):
            CURRENTRABBITPOP += 1
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    global CURRENTRABBITPOP
    global MAXRABBITPOP
    global CURRENTFOXPOP

    ate_rabbit = False

    if CURRENTRABBITPOP > 10:
        if random.random() <= float(CURRENTRABBITPOP)/MAXRABBITPOP:
            CURRENTRABBITPOP -= 1
            ate_rabbit = True
        if ate_rabbit == True:
            if random.random() <= 1/3.0:
                CURRENTFOXPOP += 1
        if ate_rabbit == False:
            if CURRENTFOXPOP >= 10:
                if random.random() <= 0.1:
                    CURRENTFOXPOP -= 1

            
def runSimulation(numSteps=200):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    foxPop = []
    rabbitPop = []
    res = ()

    for step in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbitPop.append(CURRENTRABBITPOP)
        foxPop.append(CURRENTFOXPOP)


    res += (rabbitPop, foxPop)

    # pylab!
    pylab.title('Foxes vs. the Rabbits: after {0} generations'.format(numSteps))
    pylab.xlabel('Time')
    pylab.ylabel('Population')
    pylab.plot(range(numSteps), rabbitPop, label="Rabbits", linewidth=1.2, color='blue')
    pylab.plot(range(numSteps), foxPop, label="Foxes", linewidth=1.2, color='red')
    pylab.legend(loc='best')

    pylab.show()

    return res

    # see what the early results look like
    # for it in range(30):
    #     print '{0} rabbits, {1} foxes'.format(rabbitPop[it], foxPop[it])


print runSimulation()


