gg
def dfs(graph,start,path=[]):
    for node in graph[start]:
        if not node in path:
            path=dfs(graph,node,path)
            if start != '1':
                path=path+[start]
    return path

def bfs(graph,start,path=[]):
    q=[start]
    while q:
        v=q.pop(0)
        if not v in path:
            path=path+[v]
            q=q+graph[v]
    return path

graph={}
print("Enter the number of vertices : ")
n=int(input())
for i in range (0,n):
    print("Enter the number of nodes adjacent to",i+1,"th node : " )
    m=int(input())
    print("Enter the ",m," adjacent nodes : ")
    lists=[]
    for j in range (0,m):
        temp=input()
        lists.append(temp)
    graph[str(i+1)]=lists

for keys,values in graph.items():
    print(keys,values)



temp1=dfs(graph,'1')
temp1.append('1')
print("DFS : ", temp1)
print("BFS : ", bfs(graph,'1'))
