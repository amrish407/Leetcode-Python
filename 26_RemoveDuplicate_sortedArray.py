#leetcode problem solutions with output as per their input


"""""
nums = [1,1,2]

def removeDuplicates(nums):
    j = 0

    for i in range(1,len(nums)):
        if nums[j] != nums[i]:
            j = j+1
            nums[j] = nums[i]

    return j+1

print(removeDuplicates(nums))

"""



#leetcode problem solutions as per their requirenments

from ast import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0

        for i in range(1,len(nums)):
            if nums[j] != nums[i]:
                j = j+1
                nums[j] = nums[i]

        return j+1