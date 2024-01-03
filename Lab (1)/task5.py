from queue import Queue
input=open("input5.txt", 'r')
output=open('output5.txt', 'w')
vertex,edge,des=input.readline().split()
adj_list=[[] for i in range(int(vertex)+1)]
color=[0]*(int(vertex)+1)
output_list=[]
for j in range(int(edge)):
    u,v=input.readline().split()
    adj_list[int(u)].append(int(v))
    adj_list[int(v)].append(int(u))

def Bfs(G,s,des):
    Q=Queue()
    color[s]=1
    Q.put((s,[s]))
    while not Q.empty():
        u,path=Q.get()
        if  u != int(des):
            for v in G[u]:
                if color[v]==0:
                    color[v]=1
                    Q.put((v,path+[v])) 
        else:
            mintime=len(path)-1
            output.write( "Minimum time: "+str(mintime) +"\n")
            string=""
            for i in path:
                string+=str(i)+" "
            output.write("Shortest path: " + string )
            return 
Bfs(adj_list,1,des)
  
    