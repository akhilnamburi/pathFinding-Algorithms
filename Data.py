import sys
class Data:
    def __init__(self):
        self.longDict = {}
        self.roadsDict = {}


    def readfile(self, roads, longitudes):
        with open(longitudes, 'r') as f:
            for ln in f:
                if not ln.lstrip().startswith('#'):
                    if ln.split():
                        self.longDict[ln.split()[0].capitalize()] = ln.split()[1]
        with open(roads, 'r') as f:
            key = ''
            for ln in f:
                lnList = ln.split()
                if not ln.lstrip().startswith('#') and lnList:
                    if lnList[0][-1] == ":":
                        key = lnList[0]
                        self.roadsDict[key[:-1].capitalize()] = {}
                    else:
                        tempdict =  self.roadsDict[key[:-1].capitalize()]
                        tempdict[lnList[0].capitalize()] = lnList[1]


    def startGoalCities(self):
        # arguments provided should be 2
        if len(sys.argv) != 3:
            print("Enter Source and Destination cities")
            sys.exit(0)

        start = sys.argv[1]
        goal = sys.argv[2]
        # converting city names to lowercase
        start, goal = start.capitalize(), goal.capitalize()

        # checking whether from city is present in logitude data
        if start not in self.longDict:
            print(start+ "is not a valid city")
            sys.exit(0)

        # checking whether to city is present in logitude data
        if goal not in self.longDict:
            print(goal+"is not a valid city")
            sys.exit(0)

        return start, goal