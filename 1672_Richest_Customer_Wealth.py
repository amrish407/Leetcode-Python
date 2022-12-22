#Leetcode question 1672 with input solution

"""""
accounts = [[1,2,3], [1,2,4]]

def maximumWealth(accounts):
    max = 0

    for i in range(len(accounts)):
        sum = 0

        for j in range(len(accounts[0])):
            sum += accounts[i][j]

            if max < sum :
                max = sum

    return max

print(maximumWealth(accounts))
"""



#Leetcode solutions

from ast import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0

        for i in range(len(accounts)):
            sum = 0

            for j in range(len(accounts[0])):
                sum += accounts[i][j]

                if max < sum :
                    max = sum

        return max

