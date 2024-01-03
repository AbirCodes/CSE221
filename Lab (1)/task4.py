input=open("input4.txt", 'r')
output=open('output4.txt', 'w')
vertex,edge=input.readline().split()
adj_list=[[] for i in range(int(vertex)+1)]
color=[0]*(int(vertex)+1)
for j in range(int(edge)):
    u,v=input.readline().split()
    adj_list[int(u)].append(int(v))
flag=False
def DFS(G,s):
    global flag
    color[s]=1
    for v in G[s]:
        if color[v]==0:
            DFS(G,v)
        else:
            flag=True
            break
    color[s]=0
DFS(adj_list,1)
if flag:
    print('Yes')
else:
    print('No')