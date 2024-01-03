inp=open("input6.txt", 'r')
outp=open('output6.txt', 'w')
row,col=inp.readline().split()
adj_matrix=[]

for line in inp.readlines():
    lst=[chr for chr in line.strip('\n')]
    adj_matrix.append(lst)


color=[[0]*(int(col)) for i in range(int(row))]
count=0
answer=float('-inf')

def dfs_visit(G):
    global count
    global answer
    for i in range(int(row)):
        for j in range(int(col)):
            if color[i][j] ==0 and G[i][j] != '#' and valid_index(i,j,int(row),int(col)):
                if G[i][j]=="D":
                  count=1
                else:
                   count=0
                DFS(G,(i,j))
                answer=max(answer,count)
def valid_index(i,j,r,c):
    return (i>=0 and i<= r-1) and (j>=0 and j<=c-1) 
def DFS(G,s):
    global count
    i,j=s
    color[i][j]=1
    
    if valid_index(i+1,j,int(row),int(col)) and color[i+1][j]==0 and G[i+1][j]!='#' :
        if G[i+1][j]=="D":
          count+=1
        DFS(G,(i+1,j))
    if valid_index(i-1,j,int(row),int(col)) and color[i-1][j]==0 and G[i-1][j]!='#' :
         if G[i-1][j]=="D":
          count+=1
         DFS(G,(i-1,j))
    if valid_index(i,j+1,int(row),int(col)) and color[i][j+1]==0 and G[i][j+1]!='#' :
        if G[i][j+1]=="D":
          count+=1
        DFS(G,(i,j+1))
    if valid_index(i,j-1,int(row),int(col)) and color[i][j-1]==0 and G[i][j-1]!='#' :      
        if G[i][j-1]=="D":
          count+=1
        DFS(G,(i,j-1))
     
     
dfs_visit(adj_matrix)
outp.write(f"{answer} ")
