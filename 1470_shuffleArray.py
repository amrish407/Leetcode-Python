#leetCode problem with output by giving an input

"""""
nums = [1,3,5,2,4,6]
n = 3

def shuffle(nums,n):
    
    ans =[]
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i+n])
        
    return ans

print(shuffle(nums,n))

"""""


#leetCode solution as per their requirenments


from ast import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
  
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
    
        return ans
        