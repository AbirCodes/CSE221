f=open("f:/CSE221/LabSectionNo18_22101657_CSE221LabAssignmentNo01_Fall2023/input1a.txt",'r')
f1=open("f:/CSE221/LabSectionNo18_22101657_CSE221LabAssignmentNo01_Fall2023/output1a.txt",'w')

s=f.readlines()
i=1
while i< (int(s[0])+1):
  n=int(s[i].strip())
  if n%2==0:
    f1.write(f'{n} is an Even number\n')
  else:
    f1.write(f"{n} is an Odd number\n")
  i+=1

f.close()
f1.close()

# in this code , there is only one while loop which used to check if each number of the input is even or odd. Than it writes corresponding message to the output file. Because the code has only one while loop and no other major operations are effecting time complexity, the time complexity of this code is O(n).