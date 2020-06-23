#Jump Search
'''
- Kind of a mid way between Binary Search and Linear Search

- Given an array a = [1,4,5,6,7,14,16,18,19,20] (a should be a sorted array)
  decide block size m = sqrt(n) ( where n is the size of array )

- GFG says:

What is the optimal block size to be skipped?
In the worst case, we have to do n/m jumps and if the last checked value is greater than the element to be searched for, we perform m-1 comparisons more for linear search. Therefore the total number of comparisons in the worst case will be ((n/m) + m-1). The value of the function ((n/m) + m-1) will be minimum when m = √n. Therefore, the best step size is m = √n.
'''

import numpy as np
def jumpSearch(a,m,x):
    for i in range(0,len(a),m):
        if a[i]==x:
            return i
        elif a[i]>x:
            high = i
            break
    
    for j in range(high,high-m,-1):
        if a[j]==x:
            return j
    
a = [1,4,5,6,7,14,16,18,19,20]
n = len(a)
x = 14
m = int(np.ceil(np.sqrt(n)))
idx = jumpSearch(a,m,x)
print('Element found at: ',idx)