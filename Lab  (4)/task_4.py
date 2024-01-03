
f=open("f:/CSE221/LabSectionNo18_22101657_CSE221LabAssignmentNo01_Fall2023/input4.txt",'r')
f1=open("f:/CSE221/LabSectionNo18_22101657_CSE221LabAssignmentNo01_Fall2023/output4.txt",'w')

a=f.readline()
s=f.readlines()
def lexo_sort(s):
    i=0
    while i< int(a):
        idx=i
        j=i+1
        while j< int(a):
            s[idx]=s[idx].strip()
            s[j]=s[j].strip()
            x=s[idx].split(" ")
            y=s[j].split(" ")
            if x[0] > y[0]:
                idx=j
            elif x[0]==y[0]:
                if x[6] < y[6]:
                    idx=j
            j+=1              
        s[idx],s[i]=s[i],s[idx]
        f1.write(f"{s[i]}\n")
        i+=1
lexo_sort(s)
f.close()
f1.close()

#here i have used selection here , where i have checked if the string is lexicographically prior or not by using '>'. It compare every corresponding character of both strings by using their ascii value and swaps it accordingly. because it has nested loop the time complexity will be O(n**2).