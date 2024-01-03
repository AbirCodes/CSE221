f1=open('input3.txt','r')
f2=open('output3.txt','w')
people,query=f1.readline().split(" ")

par=[None]*(int(people)+1)
friends_size=[1]*(int(people)+1)
for i in range(1,len(par)):
    par[i]=i



def find(r):
    if par[r]==r:
        return r
    return find(par[r]) 

def union(a,b):
    u=find(a)
    v=find(b)
    if u!=v:
      par[v]=u
      friends_size[u]+=friends_size[v]
    return(friends_size[u])
    


       
def friends_circle():
    for i in range(int(query)):
       a,b=f1.readline().strip().split(" ")
       f2.write(f'{union(int(a),int(b))}\n')
friends_circle()

f1.close()
f2.close()

