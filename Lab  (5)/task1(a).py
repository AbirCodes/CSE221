f=open('F:\CSE221\LabSectionNo18_22101657_CSE221LabAssignmentNo02_Fall2023/input1a.txt',"r")
f1=open('F:\CSE221\LabSectionNo18_22101657_CSE221LabAssignmentNo02_Fall2023/output1a.txt',"w")
s=f.readlines()

a=s[0]
len=a.split(" ")[0]
sum=a.split(" ")[1]
arr=s[1].split(' ')

i=0
flag=True
while i < int(a[0]):
  j=i+1
  while j<int(a[0]):
    if (int(arr[i]) + int(arr[j])) == int(sum):
      f1.write(f'{i+1} {j+1}')
      flag=False
      break
    j+=1
  i+=1
if flag==True:
   f1.write("IMPOSSIBLE")
f.close()
f1.close()