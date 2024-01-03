input=open("input3.txt", 'r')
output=open('output3.txt', 'w')
vertex,edge=input.readline().split()
adj_list=[[] for i in range(int(vertex)+1)]
color=[0]*(int(vertex)+1)
output_list=[]
for j in range(int(edge)):
    u,v=input.readline().split()
    adj_list[int(u)].append(int(v))

def DFS(G,s):
    color[s]=1
    output_list.append(s)
    for v in G[s]:
        if color[v]==0:
            DFS(G,v)
DFS(adj_list,1)
print(output_list)