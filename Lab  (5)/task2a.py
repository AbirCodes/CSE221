f=open('F:\CSE221\LabSectionNo18_22101657_CSE221LabAssignmentNo02_Fall2023/input2a.txt',"r")
f1=open('F:\CSE221\LabSectionNo18_22101657_CSE221LabAssignmentNo02_Fall2023/output2a.txt',"w")

s=f.readlines()
s[1]=s[1].strip()
arr1=s[1].split(" ")

s[3]=s[3].strip()
arr2=s[3].split(" ")

arr=arr1+arr2
for i in range(len(arr)):
    arr[i]=int(arr[i])
arr=sorted(arr)
for i in arr:
    f1.write(f"{int(i)} ")

f.close()
f1.close()