f=open('F:\CSE221\LabSectionNo18_22101657_CSE221LabAssignmentNo02_Fall2023/input2b.txt',"r")
f1=open('F:\CSE221\LabSectionNo18_22101657_CSE221LabAssignmentNo02_Fall2023/output2b.txt',"w")

s=f.readlines()
s[1]=s[1].strip()
arr1=s[1].split(" ")

s[3]=s[3].strip()
arr2=s[3].split(" ")

len1=int(s[0])
len2=int(s[2])
p1=0
p2=0
i=0
arr=[]

while i<(len1+len2):
    if  p1 !=len1 and p2!=len2:    
        if int(arr1[p1]) < int(arr2[p2]):
            arr.append((arr1[p1]))
            p1+=1
        else:
            arr.append((arr2[p2]))
            p2+=1
    i+=1
if arr1[p1:len1]:
    arr=arr+arr1[p1:len1]
if arr2[p2:len2]:
        arr=arr+arr2[p2:len2]

for i in arr:
     f1.write(f"{int(i)} ")

f.close()
f1.close()