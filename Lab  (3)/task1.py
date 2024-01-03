import heapq
f1=open('input1.txt','r')
f2=open('output1.txt','w')
vertex,edge=f1.readline().split(" ")
adj_list=[[] for i in range(int(vertex)+1)]


for i in range(int(edge)):
    u,v,w=f1.readline().strip().split(' ')
    adj_list[int(u)].append((int(v),int(w)))
source=int(f1.readline())
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
                
    for i in range(len(distance)):
        if distance[i] == float('inf'):
            distance[i]= -1        
    return distance
distance=dijkstra(adj_list,source)
for i in range(1,len(distance)):
    f2.write(f'{distance[i]} ')

f1.close()
f2.close()





