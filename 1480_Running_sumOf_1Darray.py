#Actual solution with input
"""""
nums = [1,2,3,4]

def runningSum(nums):

    for i in range(1,len(nums)):
        nums[i] = nums[i] + nums[i-1]

    return nums
print(runningSum(nums)) 
"""""


#Leetcode solutions

from ast import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]

        return nums





    
