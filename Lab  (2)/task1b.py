from queue import Queue
input=open("input1b.txt", 'r')
output=open('output1b.txt', 'w')
vertex,edge=input.readline().split()
adj_list=[[] for i in range(int(vertex)+1)]
in_degree = [0] * (int(vertex) + 1)
for j in range(int(edge)):
    u,v=input.readline().split()
    adj_list[int(u)].append(int(v))
    in_degree[int(v)]+=1

def topo_sort(G):
    Q=Queue()
    output_list=[]
    for i in range(1,len(in_degree)):
        if in_degree[i]==0:
            Q.put(i)
    
    while not Q.empty():
        u=Q.get()
        output_list.append(u)
        for v in G[u]:
            in_degree[v]-=1
            if in_degree[v]==0:
                Q.put(v)

    if len(output_list) != int(vertex):
        output.write('Impossible')
    else:
        for i in output_list:
            output.write(f"{i} ")

topo_sort(adj_list)
