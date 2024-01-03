input=open("input1a.txt", 'r')
output=open('output1a.txt', 'w')
vertex,edge=input.readline().split()
adj_list=[[] for i in range(int(vertex)+1)]
for j in range(int(edge)):
    u,v=input.readline().split()
    adj_list[int(u)].append(int(v))

output_list=[]
color=[0]*(int(vertex)+1)
cycle_check=[]
def topo_sort(G,s):        
        color[s]=1
        cycle_check.append(s)
        for v in G[s]:
            if v in cycle_check:
                output.write('Impossible')
                exit()
            if color[v]==0:
                topo_sort(G,v)
        output_list.append(s)
        cycle_check.remove(s)
for i in range(1,int(vertex)+1):
        if color[i] == 0:
            topo_sort(adj_list,i)
      
for i in range(len(output_list)-1,-1,-1):
        output.write(str(output_list[i])+' ')
