class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        counts1 = {}
        for i in s1:
            counts1[i] = 1 + counts1.get(i,0)
        for i in range(n - m + 1):
            counts2 = {}
            for j in s2[i:i+m]:
                counts2[j] = 1 + counts2.get(j,0)   
            if counts1 == counts2:
                return True
        return False