from collections import defaultdict
import random
from time import clock
import matplotlib.pyplot as plt
timy=[]
niy=[]
timy2=[]
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices


    def addEdge(self,u,v):
        self.graph[u].append(v)


    def DFSUtil(self,v,visited):


        visited[v]= True
        print v,


        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)



    def DFS(self,v):


        visited = [False]*(len(self.graph))

        
        self.DFSUtil(v,visited)
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

    for _ in range(0,N):
        v1=random.randint(1,4)
        v2=random.randint(0,2)
        g.addEdge(v1,v2);
        print(v1,v2)
    start=clock()
    g.DFS(2)
    end=clock()
    timy.append(end-start)
    start=clock()
    g.topologicalSort()

    end=clock()
    timy2.append(end-start)
    niy.append(N)
plt.plot(niy,timy,label='Topological Sort')
plt.title('Topological Sort')
plt.xlabel('N Value')
plt.ylabel('Time in seconds')
plt.grid()

plt.plot(niy,timy2,label='DFS')
plt.legend()
plt.show()
