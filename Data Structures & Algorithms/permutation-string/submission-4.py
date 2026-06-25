class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        count_s1 = {}
        count_s2 = {}
        if len(s1) >len(s2):
            return False
        for r in range(len(s1)):
            count_s1[s1[r]] = count_s1.get(s1[r],0) + 1
            count_s2[s2[r]] = count_s2.get(s2[r],0) + 1
        if count_s1 == count_s2:
            return True
        else:
            count_s2[s2[l]] -= 1
            if count_s2[s2[l]] == 0:
                count_s2.pop(s2[l])
            l += 1
        for r in range(len(s1),len(s2)):
            
            count_s2[s2[r]] = count_s2.get(s2[r],0) + 1
            print(count_s1,count_s2)
            if count_s1 == count_s2:
                return True
            count_s2[s2[l]] -= 1
            if count_s2[s2[l]] == 0:
                count_s2.pop(s2[l])
            l += 1
        
        return False
