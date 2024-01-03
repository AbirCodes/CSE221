f=open('F:\CSE221\LabSectionNo18_22101657_CSE221LabAssignmentNo02_Fall2023/input4.txt',"r")
f1=open('F:\CSE221\LabSectionNo18_22101657_CSE221LabAssignmentNo02_Fall2023/output4.txt',"w")

a=f.readlines()
t_num=int(a[0].split(" ")[0])
person=int(a[0].split(" ")[1])
arr=[]
for i in range(1,t_num+1):
    a[i]=a[i].strip()
    arr.append(a[i].split(' '))

arr.sort(key=lambda x: int(x[1]))
selected_tasks=[]
for i in range(person):
    if arr[0] not in selected_tasks:
        selected_tasks.append(arr[0])
        arr.remove(arr[0])
    new=arr.copy()
    new.sort(key=lambda x: int(x[0]))
    for j in range(len(new)):
        if selected_tasks[-1][-1] <= new[j][0]:
            selected_tasks.append(new[j])
            arr.remove(new[j])
f1.write(str(len(selected_tasks)))
f.close()
f1.close()
