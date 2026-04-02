class Solution:
    def isPalindrome(self, s: str) -> bool:

        word = ""
        for c in s:
            if c.isalpha() or c.isnumeric():
                word += c
        
        temp = word.lower()


        l = 0
        r = len(temp) - 1

        while l < r:
            if temp[l] != temp[r]:
                return False
            l += 1
            r -= 1
        
        return True