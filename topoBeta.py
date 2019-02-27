from collections import defaultdict
import random

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices


    def addEdge(self,u,v):
        self.graph[u].append(v)


    def topologicalSortUtil(self,v,visited,stack):


        visited[v] = True


        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)


        stack.insert(0,v)


    def topologicalSort(self):

        visited = [False]*self.V
        stack =[]


        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)


        print (stack)
N=6
g= Graph(N)
for _ in range(0,N):
    v1=random.randint(1,10)
    v2=random.randint(0,5)
    g.addEdge(v1,v2);
    print(v1,v2)


print ("Following is a Topological Sort of the given graph")
g.topologicalSort()
