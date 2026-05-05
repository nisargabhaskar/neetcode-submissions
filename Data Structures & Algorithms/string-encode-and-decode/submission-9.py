class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        text = ''
        for s in strs:
            text = text+str(len(s))+'#'+s
        print(text)
        return text
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        x = 0
        lastwordend = 0
        temp =[]
        while x < len(s):
            if s[x] == '#':
                count=int(s[lastwordend :x])
                lastwordend = x+1+count
                word = s[x+1:lastwordend]
                temp.append(word)
                x = lastwordend
            else:
                x += 1
        return temp