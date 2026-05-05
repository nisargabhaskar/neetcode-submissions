class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictkeys ={']':'[','}':'{',')':'('}
        ptr = -1
        for i in s:
            if i in dictkeys.values():
                ptr += 1
                stack.append(i)
            elif i in dictkeys.keys() and len(stack)>0 :
                if stack[ptr] == dictkeys[i]:
                    stack.remove(stack[ptr])
                    ptr -= 1
                else:
                    return False
            else :
                return False
        if ptr == -1:
            return True
        return False