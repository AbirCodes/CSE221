from queue import Queue
input=open("input3.txt", 'r')
output=open('output3.txt', 'w')
vertex,edge=input.readline().split()
adj_list=[[] for i in range(int(vertex)+1)]
for j in range(int(edge)):
    u,v=input.readline().split()
    adj_list[int(u)].append(int(v))
def DFS(G,s,color):
    color[s]=1
    output.write(f"{s} ")
    for v in G[s]:
        if color[v]==0:
            DFS(G,v,color)

def PDFS(G,s,priority,color):
    color[s]=1
    for v in G[s]:
        if color[v]==0:
            PDFS(G,v,priority,color)
    priority.append(s)
def tranform(G):
    TG=[[] for i in range(int(vertex)+1)]
    for v in range(1,len(G)):
        for u in G[v]:
            TG[u].append(v)
    return TG

def Kosaraju(G):
    color=[0]*(int(vertex)+1)
    priority=[]
    for v in range(1,len(G)):
        if color[v]==0:
            PDFS(G,v,priority,color)
    TG=tranform(G)
    color=[0]*(int(vertex)+1)
    while priority:
        v=priority.pop()
        if color[v]==0:
            DFS(TG,v,color)
            output.write(f"\n")        
Kosaraju(adj_list)
     

