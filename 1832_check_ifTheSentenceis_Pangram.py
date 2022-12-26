#leetCode problem solutions with Output as per their input

"""""

sentence = "thequickbrownfoxjumpsoverthelazydog"

import string
class Solution:
    def checkIfPangram(sentence: str) -> bool:
        for i in string.ascii_lowercase[:26]:
            if i not in sentence:
                return False
        return True
    
    print(checkIfPangram(sentence))    

"""    

#leetCode problem solutions as per their requirenments

import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for i in string.ascii_lowercase[:26]:
            if i not in sentence:
                return False
        return True