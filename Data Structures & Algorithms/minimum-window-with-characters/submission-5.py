class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if set(t) != {x for x in s if x in t} or len(s)<len(t):
            return ''
        else :
            countt = {}
            m = len(t)
            for i in t:
                countt[i] = 1 + countt.get(i,0)
            n = len(s)
            l = 0
            minlength = n
            res = ''
            while l < n - m +1:
                if s[l] in t:
                    counts = {}
                    for i in s[l:l+m]:
                        if i in t:
                            if counts.get(i,0) < countt[i]:
                                counts[i] = 1 + counts.get(i,0)
                    inc = 0
                    while countt != counts and l + m + inc < n:
                        if s[l+m+inc] in t:  
                            if counts.get(s[l+m+inc],0) < countt[s[l+m+inc]]:
                                counts[s[l+m+inc]] = 1 + counts.get(s[l+m+inc],0)
                        inc += 1
                    # print(countt,counts)
                    if countt == counts and len(s[l:l+m+inc]) <= minlength:
                        res = s[l:l+m+inc]
                        minlength = len(s[l:l+m+inc])
                l += 1
            return res
