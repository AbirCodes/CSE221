from queue import Queue
input=open("input2.txt", 'r')
output=open('output2.txt', 'w')
vertex,edge=input.readline().split()
adj_list=[[] for i in range(int(vertex)+1)]
color=[0]*(int(vertex)+1)
output_list=[]
for j in range(int(edge)):
    u,v=input.readline().split()
    adj_list[int(u)].append(int(v))

def Bfs(G,s):
    Q=Queue()
    color[s]=1
    output_list.append(s)
    Q.put(s)
    while not Q.empty():
        u=Q.get()
        for v in G[u]:
            if color[v]==0:
                color[v]=1
                Q.put(v) 
                output_list.append(v)

Bfs(adj_list,1)
print(output_list)  
    