f1=open('input2.txt','r')
f2=open('output2.txt','w')
a=f1.readlines()
arr=a[1].split(" ")
arr=[int(x) for x in arr]
def maximum(arr,r=0,l=len(arr)-1):

    if l==r:
      return arr[l]
    
    mid=(l+r)//2

    left=maximum(arr,r,mid)
    right=maximum(arr,mid+1,l)

    return max(right,left)
f2.write(str(maximum(arr)))
f1.close()
f2.close()