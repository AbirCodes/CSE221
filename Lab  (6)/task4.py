f1=open('input4.txt','r')
f2=open('output4.txt','w')
a=f1.readlines()
arr=a[1].split(" ")
arr=[int(x) for x in arr]
def maximum(arr,mid):
    i,j,max1,max2=0,mid,-99999,-99999
    while i< mid:
        if arr[i]>max1:
            max1=arr[i]
        i+=1
        
    while j< len(arr):
        if arr[j]**2 > max2:
            max2=arr[j]**2
        j+=1       
    return max1+max2

def max_value(arr):
    if len(arr) ==1:
        return float('-inf')
    elif len(arr) ==2:
        return int(arr[0]+arr[1]**2)
    
    mid=len(arr)//2
    a1=max_value(arr[:mid])
    a2=max_value(arr[mid:])
    max2=maximum(arr,mid)
    return max(a1,a2,max2)
    
   
f2.write(str(max_value(arr)))
f1.close()
f2.close()
