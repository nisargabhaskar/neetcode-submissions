class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        for i in range(n):
            subs = ''
            x = i
            while x < n and s[x] not in subs:
                subs += s[x]
                x += 1
            l = max(l,len(subs))
        return l