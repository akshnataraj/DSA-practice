'''
Algorithm:
Logic based on the fact that one of the subarrays will be sorted!
https://stackoverflow.com/questions/4773807/searching-in-a-sorted-and-rotated-array
 '''

 def searchArray(a,low,high,x):
    mid = int((low + high)/2)
#     print(a[mid])

    if a[mid]==x:
        return mid
    if low>high:
        return -1
    
    if a[low]<=a[mid]: #left array is sorted
        if a[low]>=x and a[mid]<=x:
            return searchArray(a,low,mid-1,x)
        else:
            return searchArray(a,mid+1,high,x)
    else: #right array is sorted
        print(a[mid],a[high])
        if a[mid]<=x and a[high]>=x:
            return searchArray(a,mid+1,high,x)
        else:
            return searchArray(a,low,mid-1,x)

a = [4,5,1,2,3]
x = 5
low = 0
high = len(a)-1
idx = searchArray(a,low,high,x)
print('Indexed at idx: ',idx)