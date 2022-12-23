#leetCode problem solution with output by giving an input

"""""

nums = [1,2,3,1,1,3]

class Solution:
    def numIdenticalPairs(nums):
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] == nums[j] and i<j:
                    count = count+1

        return count
    
    print(numIdenticalPairs(nums))

"""

#leetCode problem solution as per their requirenments

from ast import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] == nums[j] and i<j:
                    count = count+1

        return count