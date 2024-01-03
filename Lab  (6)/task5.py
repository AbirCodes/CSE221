f1=open('input5.txt','r')
f2=open('output5.txt','w')
a=f1.readlines()
arr=a[1].split(" ")
arr=[int(x) for x in arr]

def QuickSort(arr,p,r):
    if p<r:
        q=Partition(arr,p,r)
        QuickSort(arr,p,q-1)
        QuickSort(arr,q+1,r)

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

QuickSort(arr,0,len(arr)-1)
for i in arr:
    f2.write(f"{i} ")



f1.close()
f2.close()