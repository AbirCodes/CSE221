f1=open('input1.txt','r')
f2=open('output1.txt','w')
a=f1.readlines()
arr=a[1].split(" ")
arr=[int(x) for x in arr]
def merge(a,b):
  sorted_arr=[]
  i,j=0,0
  while i < len(a) and j < len(b):
      if a[i] > b[j]:
          sorted_arr.append(b[j])
          j += 1
      else:
          sorted_arr.append(a[i])
          i += 1

  sorted_arr += a[i:]
  sorted_arr += b[j:]

  return sorted_arr
  
def mergeSort(arr):
  if len(arr) <= 1:
     return arr
  else:
    mid = len(arr)//2
    a1 = mergeSort(arr[:mid]) 
    a2 = mergeSort(arr[mid:]) 
    return merge(a1, a2) 

for i in mergeSort(arr):
   f2.write(f'{i} ')
f1.close()
f2.close()
