import heapq
f1=open('input2.txt','r')
f2=open('output2.txt','w')
vertex,edge=f1.readline().split(" ")
adj_list=[[] for i in range(int(vertex)+1)]


for i in range(int(edge)):
    u,v,w=f1.readline().strip().split(' ')
    adj_list[int(u)].append((int(v),int(w)))
start_node,end_node=f1.readline().split()
def dijkstra(G,s):
    distance=[float('inf')]*(int(vertex)+1)
    distance[s]=0
    min_Q=[(s,0)]
    for v in range(1,int(vertex)+1):
        heapq.heappush(min_Q,(v,distance[v]))
    while min_Q:
        u,dist=heapq.heappop(min_Q)       
        for v,w in G[u]:
            new_dst= dist + w
            if new_dst < distance[v]:
                distance[v]=new_dst
                heapq.heappush(min_Q,(v,distance[v]))       
    return distance
time1=dijkstra(adj_list,int(start_node))
time2=dijkstra(adj_list,int(end_node))


time_to_reach=float('inf')
common_node=float('inf')
for i in range(1,int(vertex)+1):
    if time1[i] < float('inf') and time2[i] < float('inf'):
        max_time=max(time1[i],time2[i])
        if max_time < time_to_reach:
            time_to_reach=max_time
            common_node=i
if common_node !=float('inf'):
    f2.write(f'Time {time_to_reach}\nNode {common_node}')
else:
    f2.write("Impossible")




f1.close()
f2.close()

