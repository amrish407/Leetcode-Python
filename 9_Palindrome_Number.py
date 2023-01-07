#leetcode problem solutions with output as per their input


"""""
x = 121

def isPalindrome(x):
    x_str = str(x)
    x_str_rev = ""
    for i in range(len(x_str)):
        x_str_rev += x_str[-i-1]
    return x_str_rev == x_str
print(isPalindrome(x))

"""



#leetcode problem solutions with their requirenments

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_str_rev = ""
        for i in range(len(x_str)):
            x_str_rev += x_str[-i-1]
        return x_str_rev == x_str