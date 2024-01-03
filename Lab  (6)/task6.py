f1=open('input6.txt','r')
f2=open('output6.txt','w')
a=f1.readline().strip()
arr=f1.readline()
arr=arr.split(" ")
arr=[int(x) for x in arr]
query_number=f1.readline().strip()

def Partition(arr,p,r):
    pivot=arr[r]
    i=p-1
    j=p
    while j< r:
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

def kth_smallest(arr,l,r,k):
    if l==r:
        return arr[l]
    idx=Partition(arr,l,r)
    if idx==k:
        return arr[idx]
    elif idx>k:
        return kth_smallest(arr,l,idx-1,k)
    else:
        return kth_smallest(arr,idx+1,r,k)

for i in range(int(query_number)):
    k=f1.readline().strip()
    f2.write(f'{str(kth_smallest(arr,0,int(a)-1,int(k)-1))}\n')
    
f1.close()
f2.close()
