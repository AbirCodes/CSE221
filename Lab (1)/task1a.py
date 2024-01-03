input=open('input1a.txt','r')
output=open('output1a.txt','w')

vertex,edge=input.readline().split()
matrix=[[0]*(int(vertex)+1) for i in range(int(vertex)+1)]

for i in range(int(edge)):
    u,v,w=input.readline().split()
    matrix[int(u)][int(v)]=int(w)
for i in matrix:
    i=str(i).strip("[]")
    output.write(f'{i}\n')



input.close()
output.close()