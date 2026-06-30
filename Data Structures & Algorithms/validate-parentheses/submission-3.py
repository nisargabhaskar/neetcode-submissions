class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parantheses_map = { '{' : '}','(':')','[':']'}
        for b in s:
            if b in ['{','[','(']:
                stack.append(parantheses_map[b])
            else:
                if not stack or stack.pop() != b:
                    return False
        return len(stack) == 0