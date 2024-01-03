input=open('input1b.txt','r')
output=open('output1b.txt','w')

vertex,edge=input.readline().split()
adj_list=[[] for i in range(int(vertex)+1)]

for i in range(int(edge)):
    u,v,w=input.readline().split()
    adj_list[int(u)].append((v,w))
for i in range(int(vertex)+1):
    out=str(adj_list[i]).strip('[]')
    output.write(f'{i} : {out}\n')

input.close()
output.close()