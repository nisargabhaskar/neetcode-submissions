class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0, len(s) - 1
        while r > -1 and not s[r].isalnum() :
            r -= 1
        
        while l < len(s) and not s[l].isalnum() :
            l += 1
        while l < r:
            if  s[l].lower() == s[r].lower():
                r -= 1
                l += 1
            else :
                return False
            while r > -1 and not s[r].isalnum() :
                r -= 1
            while l < len(s) and not s[l].isalnum() :
                l += 1
        return True