f1=open('input3.txt','r')
f2=open('output3.txt','w')
a=f1.readlines()
arr=a[1].split(" ")
arr=[int(x) for x in arr]
def conquer(a,b):
  sorted_arr=[]
  i,j,count=0,0,0
  while i < len(a) and j < len(b):
      if a[i] > b[j]:
          sorted_arr.append(b[j])
          count+=len(a[i:])
          j += 1
      else:
          sorted_arr.append(a[i])
          i += 1
  sorted_arr += a[i:]
  sorted_arr += b[j:]
  return sorted_arr,count
  
def Divide(arr):
  if len(arr) <= 1:
     return arr,0
  else:
    mid = len(arr)//2
    a1,count1 = Divide(arr[:mid]) 
    a2,count2 = Divide(arr[mid:]) 
    a3,count3= conquer(a1, a2) 
    return a3,count1+count2+count3
  
f2.write(str(Divide(arr)[1]))

f1.close()
f2.close()