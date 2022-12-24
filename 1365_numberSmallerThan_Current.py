#leetCode problem solution with an output as per their given input

"""""

nums = [8,1,2,2,3]

def smallerNumbersThanCurrent(nums):
    ans = []
        

    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count = count + 1
        ans.append(count)

    return ans

print(smallerNumbersThanCurrent(nums))

"""



#leetCode problem solutions as per their requirenments

from ast import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        

        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count = count + 1
            ans.append(count)

        return ans