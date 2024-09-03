class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graphdict = {} #We are transforming tuple to dictionary 
        for start,end in self.edges: #To go through all the edges
            if start in  self.graphdict: #In this condition there is already some data in dictionary
                self.graphdict[start].append(end) #Here If we need to give a value to same key
            else: #Here dictionary is blank
                self.graphdict[start] = [end] #Here we gave a coonection to key and value Now see if condition
        print("Graph dict",self.graphdict)

    def GetPath(self,start,end,path = []): #Here we will give start and end value and function will return all possible paths
#It will follow recursive approach. Here we will first all nodes connected to end and then we will prefix(append) start 
        path = path+[start] #Path is empty list with only start value
        if start == end:   
            return[path]
        if start not in self.graphdict: #corner case Like path between Toronto and Mumbai
            return[]
        #Now for regular case For ex- Mumbai to NewYork
        Paths = []
        for node in self.graphdict[start]: #This for loop will traverse nodes of start (here nodes of Mumbai i.e. Paris and NewYork )
            if node not in path: #If the node is not added before in list so will add it in list using recursion (Here if Mumbai is start node its in the list but its node paris is not in list)
                NewPath = self.GetPath(node,end,path) 
                for p in NewPath: #This for loop appends those value in Paths(main list)
                    Paths.append(p)
        return Paths            


    def GetShortestPath(self,start,end,path=[]):
        path = path+[start]
        if start == end:
            return path
        if start not in self.graphdict:
            return None

        ShortestPath = None   
        for node in self.graphdict[start]:
            if node not in path:
                sp = self.GetShortestPath(node,end,path)
                if sp:
                    if ShortestPath is None or len(sp) < len(ShortestPath):
                        ShortestPath =sp
        return ShortestPath                





if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    RouteGraph = Graph(routes)

    start = "Mumbai"
    end = "New York"
    print("Paths between {start} and {end}:", RouteGraph.GetPath(start,end))
    print("Shortest path between {start} and {end}:", RouteGraph.GetShortestPath(start,end))