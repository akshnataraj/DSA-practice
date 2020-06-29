'''Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

def maxSubArray(self, nums: List[int]) -> int:
max_elem = nums[0]
current_sum = 0
for i in nums:
    if current_sum < 0: #because we care only about "maximum" subarray
        current_sum = 0
    current_sum += i
    max_elem = max(current_sum, max_elem)
    
return max_elem

#Still have to figure out the divide and conquer approach!