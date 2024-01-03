f=open("f:/CSE221/LabSectionNo18_22101657_CSE221LabAssignmentNo01_Fall2023/input1b.txt",'r')
f1=open("f:/CSE221/LabSectionNo18_22101657_CSE221LabAssignmentNo01_Fall2023/output1b.txt",'w')

s=f.readlines()
i=1
while i< (int(s[0])+1):
  n=s[i].strip()
  val=n.split(" ")
  if val[2] =="+":
    result=int(val[1])+int(val[3])
    f1.write(f"The result of {val[1]} + {val[3]} is  {result}\n")
  elif val[2] =="-":
    result=int(val[1])-int(val[3])
    f1.write(f"The result of {val[1]} - {val[3]} is  {result}\n")

  elif val[2] =="*":
    result=int(val[1])*int(val[3])
    f1.write(f"The result of {val[1]} * {val[3]} is  {result}\n")

  elif val[2] =="/":
    result=int(val[1] )/ int(val[3])
    f1.write(f"The result of {val[1]} / {val[3]} is  {result}\n")
  i+=1

f.close()
f1.close()

# in this code , there is only one while loop which used to perform corresponding operations over each number given in the iniput file. Than it writes corresponding message to the output file. Because the code has only one while loop and no other major operations are effecting time complexity, the time complexity of this code is O(n).