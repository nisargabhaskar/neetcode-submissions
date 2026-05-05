class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x.lower() for x in s if x.isalnum() ]
        s = ''.join(s)
        if s == s[::-1]:
            return True
        else :
            return False