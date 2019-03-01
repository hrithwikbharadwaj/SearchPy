from collections import defaultdict
import random
from time import clock
import matplotlib.pyplot as plt
timy=[]
niy=[]
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
for N in range(10000, 50000, 10000):
    g= Graph(N)
    start=clock()
    for _ in range(0,N):
        v1=random.randint(1,9)
        v2=random.randint(0,9)
        g.addEdge(v1,v2);
        print(v1,v2)
    g.topologicalSort()
    end=clock()
    timy.append(end-start)
    niy.append(N)
plt.plot(niy,timy)
plt.show()
