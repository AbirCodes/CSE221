f=open("f:/CSE221/LabSectionNo18_22101657_CSE221LabAssignmentNo01_Fall2023/input2.txt",'r')
f1=open("f:/CSE221/LabSectionNo18_22101657_CSE221LabAssignmentNo01_Fall2023/output2.txt",'w')


a=f.readlines()
arr=a[1].split(' ')

def bubbleSort(arr):
    for i in range(len(arr)-1):
        flag=False
        for j in range(len(arr)-i-1):
            if int(arr[j]) > int(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                flag=True
        if flag == False:
             break

    for i in arr:
        f1.write(f'{i} ')
bubbleSort(arr)
## the best case is when the array is already sorted.
##because no element will be needed to be swapped, thats why it won't enter the if condition and the flag value will remain false.
## and after the first iteration of the first loop the code will break which will save time.
##hence the time complexity will be reduced to O(n) for the best case. Where n is the number of inputs.

f.close()
f1.close()
