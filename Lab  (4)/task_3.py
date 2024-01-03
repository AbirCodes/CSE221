f=open("f:/CSE221/LabSectionNo18_22101657_CSE221LabAssignmentNo01_Fall2023/input3.txt",'r')
f1=open("f:/CSE221/LabSectionNo18_22101657_CSE221LabAssignmentNo01_Fall2023/output3.txt",'w')

a=f.readlines()
roll=a[1].strip()
marks=a[2].strip()
roll=roll.split(' ')
marks=marks.split(' ')
def sort(marks,roll):
    i=0
    while i < int(a[0]):
        idx = i
        j=i+1
        while j<int(a[0]):
            if int(marks[idx]) < int( marks[j]):
                idx = j
            elif int(marks[idx]) == int(marks[j]):
                if int(roll[idx]) > int(roll[j]):
                    idx = j
            j+=1
        marks[i], marks[idx] = marks[idx], marks[i]
        roll[i],roll[idx]=roll[idx],roll[i]
        f1.write(f'ID: {roll[i]} , Marks: {marks[i]}\n')
        i+=1
sort(marks,roll)
f.close()
f1.close()

#here i have used selection sort, because the task required minimum swapping and selection sort does minimum swapping while sorting the values. here i have given two coditions , in the first condition i have priotized the bigger marks and swapped the id number according to it also. in next condition if both marks are same than i have priotized the smaller id number. because there are nested loops working here the time complexity will be, O(n**2) 