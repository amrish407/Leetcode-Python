#leetCode problem solution with output as per their input

"""""

nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    ans = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                ans.append(i)
                ans.append(j)

    return ans

print(twoSum(nums,target))

"""


#leetCode problem solution as per their requirenments


from ast import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)

        return ans