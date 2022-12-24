#leetCode problem solution with an output as per their input 

"""""

nums = [0,1,2,3,4] 
index = [0,1,2,2,1]

def createTargetArray(nums,index):
    target = []

    for i in range(len(nums)):
        target.insert(index[i],nums[i])

        for i in range(len(target)):
            index[i] = target[i]

    return index
print(createTargetArray(nums,index))

"""

#leetCode problem solution as per their requirenments

from ast import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []

        for i in range(len(nums)):
            target.insert(index[i],nums[i])

            for i in range(len(target)):
                index[i] = target[i]

        return index