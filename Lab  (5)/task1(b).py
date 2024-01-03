f=open('F:\CSE221\LabSectionNo18_22101657_CSE221LabAssignmentNo02_Fall2023/input1b.txt',"r")
f1=open('F:\CSE221\LabSectionNo18_22101657_CSE221LabAssignmentNo02_Fall2023/output1b.txt',"w")
s=f.readlines()

a=s[0]
len=a.split(" ")[0]
sum=a.split(" ")[1]
arr=s[1].split(' ')

l=0
r=int(a[0])-1
while l<r:
  if (int(arr[l])+int(arr[r])) > int(sum):
    r=r-1
  elif (int(arr[l])+int(arr[r])) < int(sum):
    l=l+1
  elif (int(arr[l])+int(arr[r])) == int(sum):
    f1.write(f"{l+1} {r+1}")
    break
if l>=r:
  f1.write("IMPOSSIBLE")
f.close()
f1.close()