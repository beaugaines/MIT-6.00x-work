class Node(object):
    def __init__(self, name):
        self.name = str(name)

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):
    """return an edge object"""
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return str(self.src) + '->' + str(self.dest)


class WeightedEdge(Edge):
    """return a weighted edge object"""
    def __init__(self, src, dest, weight=1.0):
        self.src = src
        self.dest = dest
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return str(self.src) + '->('\
          + str(self.weight) + ')'\
          + str(self.dest)


        
        
