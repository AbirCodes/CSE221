f=open('F:\CSE221\LabSectionNo18_22101657_CSE221LabAssignmentNo02_Fall2023/input3.txt',"r")
f1=open('F:\CSE221\LabSectionNo18_22101657_CSE221LabAssignmentNo02_Fall2023/output3.txt',"w")


a=f.readlines()
arr=[]
for i in range(1,int(a[0])+1):
    a[i]=a[i].strip()
    arr.append(a[i].split(' '))

arr.sort(key=lambda x: int(x[1]))
task=0
end_time=0
selected_task=""
for i in range (len(arr)):
    if int(arr[i][0])>= end_time:
        task+=1
        end_time=int(arr[i][1])
        selected_task+=f"{arr[i][0]} {arr[i][1]}\n"
f1.write(f'{task}\n{selected_task}')
f.close()
f1.close()