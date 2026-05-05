class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return []
            
        def dfs(i,wrd):
            if i >= len(digits):
                res.append(wrd)
                return
            exp = digitToChar[digits[i]]
            for x in exp:
                dfs(i+1,wrd + x)
        
        dfs(0,'')
        return res