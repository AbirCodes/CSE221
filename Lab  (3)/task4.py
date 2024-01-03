f1=open('input4.txt','r')
f2=open('output4.txt','w')
city,roads=f1.readline().split(" ")
city_roads=[]
for i in range(int(roads)):
    u,v,w=f1.readline().strip().split(" ")
    city_roads.append([int(u),int(v),int(w)])

par=[None]*(int(city)+1)
rank=[0]*(int(city)+1)
for i in range(1,len(par)):
    par[i]=i

def find(r):
    if par[r]==r:
        return r
    return find(par[r]) 

def union(a,b):
    u=find(a)
    v=find(b)
    if rank[u] < rank[v]:
        par[u]=v
    elif rank[u]>rank[v]:
        par[v]=u
    else:
        par[u]=v
        rank[v]+=1
def kruskal(city_roads):
    city_roads.sort(key=lambda i:i[2])
    cost=0
    for i in city_roads:
        u,v,w=i
        par1=find(u)
        par2=find(v)
        if par1!=par2:
            cost+=w
            union(u,v)
    return cost  
f2.write(f'{kruskal(city_roads)}')
f1.close()
f2.close()

