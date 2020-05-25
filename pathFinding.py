#!/usr/bin/python3

from Data import Data
from Node import Node
# parent class
class Main:
    def __init__(self):
        self.children, self.newChildren,  self.openList, self.closedList= ([] for i in range(4))
        self.NodeCount = self.currentNode =  0

    def __str__(self):
        return "Children are ("+ self.getList(self.children)+")\nNew children are ("+self.getList(self.newChildren)+")\nOpen list is ("+self.getList(self.openList)+")\nClosed list is ("+self.getList(self.closedList)+")\n"

    # returns the list format for children, new children, open list, closed list
    def getList(self, arg):
        value = " ".join(list(map(lambda x: x.name, arg))).strip()
        return "Nil" if value.strip()=="" else value

    # main function which has the algorithm logic
    def expand(self, data: Data, goal):
        return True

    # returns the path from origin to destination
    def finalPath(self):
        solution = [self.currentNode]
        while solution[0].parentName:
            solution = [solution[0].parentName] + solution
        return solution
"""
Bfs, Dfs, Dfid main class where expand is traversed through the map and gives path for start and goal state.
"""
class BfsDfsDfid(Main):
    def __init__(self,max_depth):
        super().__init__()
        self.max = max_depth
        self.dropped_nodes = []
        self.totalCount = 0
        self.removedNode=[]

    def bfsexpand(self,  Data,start, goal):
        self.openList.append(Node(start))
        while "True":
            if not self.openList:
                return False
            self.currentNode = self.openList.pop(0)
            print("Expanding", self.currentNode.name)
            if self.currentNode.name == goal:
                return False
            self.NodeCount += 1
            s = sorted(data.roadsDict[self.currentNode.name].keys())
            self.closedList.append(self.currentNode)
            self.children = [Node(city, self.currentNode) for city in s]
            n = [node.name for node in self.openList + self.closedList]
            combined = lambda x: x.name not in n
            self.newChildren = list(filter(combined, self.children))
            self.openList.extend(self.newChildren)
            print(dataPrinting(self.children, self.newChildren, self.openList, self.closedList))

    def dfsexpand(self,  Data, goal, depth = -1):
        # if no more nodes are available to expand
        if not self.openList:
            return False
        self.currentNode = self.openList.pop(0)
        print("Expanding", self.currentNode.name)
        # if destination city has been reached
        if self.currentNode.name == goal:
            return False
        self.NodeCount += 1
        # when current node's depth reaches max depth (in case of DFID)
        if self.currentNode.f == depth:
            print("Depth has been reached")
            self.closedList.append(self.currentNode)
            self.children = []
            return True
        # getting list of children sorted by city names in alphabetical order
        roadsList = sorted(data.roadsDict[self.currentNode.name].keys())
        self.children = [Node(city, self.currentNode, self.currentNode.f + 1) for city in roadsList]
        self.newChildren = list(filter(lambda x: x.name not in [node.name for node in self.openList + self.closedList], self.children))
        self.openList = self.newChildren + self.openList
        self.closedList.append(self.currentNode)
        return True

    def dfsexpand(self,  Data, goal, depth = -1):
        # if no more nodes are available to expand
        if not self.openList:
            return False
        self.currentNode = self.openList.pop(0)
        print("Expanding", self.currentNode.name)
        # if destination city has been reached
        if self.currentNode.name == goal:
            return False
        self.NodeCount += 1
        # when current node's depth reaches max depth (in case of DFID)
        if self.currentNode.f == depth:
            print("Depth has been reached")
            self.closedList.append(self.currentNode)
            self.children = []
            return True
        # getting list of children sorted by city names in alphabetical order
        roadsList = sorted(data.roadsDict[self.currentNode.name].keys())
        self.children = [Node(city, self.currentNode, self.currentNode.f + 1) for city in roadsList]
        # removing children which are already present in open or closed list
        self.newChildren = list(filter(lambda x: x.name not in [node.name for node in self.openList + self.closedList], self.children))
        # adding new children at the start of open list
        self.openList = self.newChildren + self.openList
        self.closedList.append(self.currentNode)
        return True

    def DFIDexpand(self,  Data, start, goal):
        # iterating from depth 0 to max depth
        for i in range(self.max + 1):
            print("\nDFID LEVEL {0} :\n".format(i))
            super().__init__()
            self.openList.append(Node(start, None, 0))
            while self.dfsexpand( data, goal, i):
                revalued_children = []
                self.removedNode = []
                # checking for revalued children
                for node in self.children:
                    for nodeList in self.closedList:
                        # find node in closed list with same name and a lower f value (depth)
                        if node.name == nodeList.name and node.f < nodeList.f:
                            revalued_children.append(node)
                            self.removedNode.append(nodeList)
                # if there are any nodes dropped
                if self.removedNode:
                    # removing dropped nodes from closed list
                    self.closedList = list(filter(lambda x: x not in self.removedNode, self.closedList))
                    # clearing open list temporarily in order to add children in sorted order later
                    self.openList = self.openList[len(self.newChildren):]
                    # sorting children list based on name
                    self.newChildren = sorted(revalued_children + self.newChildren, key = lambda x: x.name)
                    # adding new children to start of open list
                    self.openList = self.newChildren + self.openList
                print(printing1(self.removedNode,self.children,self.newChildren,self.openList,self.closedList))
            self.totalCount += self.NodeCount

def printing1(removedNode,children,newChildren,openList,closedList):
    children_info = ""
    if children:
        dropped_node_info = ""
        if removedNode:
            for node in removedNode:
                dropped_node_info += "* Dropping ( "+getNodeList1(node).strip('()')+ ") from closed list because new value is better\n"
        children_info = "Children are "+getList1(children)+"\n"+dropped_node_info+"New or revalued children are "+getList1(newChildren)+"\n"
    return children_info + "Open list is "+ getList1(openList)+"\nClosed list is "+ getList1(closedList)+"\n"

    # returns string format of nodes to be printed inside lists
def getNodeList1(node):
    return "("+(" ".join([node.name, str(node.f)]).strip())+")"


def getList1(arg):
    value = [getNodeList1(node) for node in arg]
    return "("+(" ".join(value).strip())+")" if value else "Nil"

"""
A star class for both h=0 and h= East-West distance
"""
class AStarState(Main):
    def __init__(self):
        super().__init__()

    def expand(self,  Data, goal, hValue):
        if not self.openList:
            return False
        self.currentNode = self.openList.pop(0)
        print("Expanding", self.nodeFormat(self.currentNode))
        if self.currentNode.name == goal:
            return False
        self.closedList.append(self.currentNode)
        self.NodeCount += 1
        self.children = [Node(city, self.currentNode, None, self.currentNode.g + int(distance), hValue(city, goal)) for city,distance in sorted(data.roadsDict[self.currentNode.name].items(), key=lambda x: x[0])]
        self.print_children()
        self.newChildren = list(filter(lambda x: x.name not in [node.name for node in self.closedList], self.children))
        for neighbour in self.newChildren:
            neighbour_added = False
            for openNode in self.openList:
                # check node is already present in open list
                if openNode.name == neighbour.name:
                    neighbour_added = True
                    if neighbour.f < openNode.f:
                        print("***Revaluing open node "+neighbour.name+" from "+str(openNode.f)+" to "+str(neighbour.f))
                        openNode.f,openNode.g,openNode.h = neighbour.f,neighbour.g,neighbour.h
                    break
            #node is not present in open list
            if not neighbour_added:
                self.openList.append(neighbour)
        self.openList = sorted(self.openList, key = lambda x: (x.f, self.getIndex(x.name)))
        return True

    def getIndex(self, name):
        for i in range(len(self.newChildren)):
            if self.newChildren[i].name == name:
                return i

    def print_children(self):
        value = " ".join(list(map(lambda x: x.name, self.children))).strip()
        print("Children are ", end="")
        if value.strip() == "":
            print("Nil")
        print("("+value+")")

    # returns node format for expanding info
    def nodeFormat(self, node: Node):
        return node.name+" f= "+str(node.f)+" , g= "+str(node.g)+", h= "+str(node.h)

    def getNodeList(self, node: Node):
        return "("+(" ".join([node.name, str(node.f)]).strip())+")"

    def getList(self, arg):
        value = [self.getNodeList(node) for node in arg]
        return "(" + (" ".join(value).strip()) + ")" if value else "Nil"

    def __str__(self):
        return "Open list is "+self.getList(self.openList)+"\nClosed list is "+self.getList(self.closedList)+"\n"

def dataPrinting(children,newChildren,openList,closedList):
    return "Children are "+ getList(children)+"\nNew children are "+getList(newChildren)+"\nOpen list is "+getList(openList)+"\nClosed list is "+getList(closedList)+"\n"

    # returns the list format for children, new children, open list, closed list
def getList(arg):
    value = " ".join(list(map(lambda x: x.name, arg))).strip()
    return "Nil" if value.strip()=="" else "("+value+")"

"""
execute Bfs class and print the data
"""
def bfs(data: Data, start, goal):
    print("BFS:\n\n")
    bfs_state = BfsDfsDfid(0)
    # adding origin city node to open list
    bfs_state.bfsexpand(data, start, goal)
    print("\n\nBreadth-first search solution: {0} .".format(getList(bfs_state.finalPath())))
    print(str(bfs_state.NodeCount)+" nodes expanded.")

"""
execute Dfs class and print the data
"""
def dfs(data: Data, start, goal):
    print("\n\nDFS:\n\n")
    dfs_state = BfsDfsDfid(0)
    dfs_state.openList.append(Node(start))
    while dfs_state.dfsexpand(data, goal):
        print(dfs_state)
    print("\n\nDepth-first search solution: ")
    print(getList(dfs_state.finalPath())+ " .", sep=" ")
    print(str(dfs_state.NodeCount)+" nodes expanded.")

"""
execute A star class with h=0 and print the data
"""
def aStar(data: Data, start, goal):
    print("\n\nA* WITH H=0 : \n\n")
    # initializing state
    astar_state = AStarState()
    # adding origin city node to open list
    astar_state.openList.append(Node(start))
    while astar_state.expand(data, goal, lambda x, y: 0):
        print(astar_state)
    print("\n\nA-star-search solution with H=0 : "+getList(astar_state.finalPath())+" .")
    print("Path-length: {0} .".format(astar_state.currentNode.f))
    print(str(astar_state.NodeCount)+" nodes expanded.")
"""
execute A star class with h=East-west distance and print the data
"""
def aStarWithH(data: Data, start, goal):
    print("\n\nA* WITH H=EAST-WEST DISTANCE : \n\n")
    hValue = lambda x, y: 8*abs(int(data.longDict[x]) - int(data.longDict[y]))
    astar_state = AStarState()
    astar_state.openList.append(Node(start, None, None, 0, hValue(start, goal)))
    while astar_state.expand(data, goal, hValue):
        print(astar_state)
    print("\n\nA-star-search solution with H=EAST-WEST DISTANCE : "+getList(astar_state.finalPath())+" .")
    print("Path-length: {0} .".format(astar_state.currentNode.f))
    print(str(astar_state.NodeCount)+" nodes expanded.")
"""
execute Dfid class and print the data
"""
def DFID(data: Data, start, goal):
    print("\n\nDFID: \n\n")
    dfid_state = BfsDfsDfid(3)
    dfid_state.openList.append(Node(start))
    dfid_state.DFIDexpand(data, start, goal)
    print("\n\nDFID solution: ")
    print (getList(dfid_state.finalPath()) + " .")
    print(str(dfid_state.totalCount)+" total nodes expanded.")


data = Data()
data.readfile("france-roads1.txt","france-long1.txt")
start, goal = data.startGoalCities()
bfs(data, start, goal)
dfs(data, start, goal)
aStar(data, start, goal)
aStarWithH(data, start, goal)
DFID(data, start, goal)

