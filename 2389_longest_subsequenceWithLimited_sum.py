#leetCode problem solution with output as per their input

"""""

nums = [4,5,2,1]
queries = [3,10,21]

def answerQueries(nums, queries):
    ans=[]
    nums.sort()
    for i in queries:
        c=0
        sum1=0
        for j in range(len(nums)):
            if sum1+nums[j]<=i:
                sum1+=nums[j]
                c=c+1
        ans.append(c)
    return ans
    
print(answerQueries(nums,queries))

"""

#leetCode as per their solutions

from ast import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        for i in queries:
            c=0
            sum1=0
            for j in range(len(nums)):
                if sum1+nums[j]<=i:
                    sum1+=nums[j]
                    c=c+1
            ans.append(c)
        return ans