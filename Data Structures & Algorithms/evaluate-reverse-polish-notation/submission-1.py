class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []   
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(int(i)) 
            else:
                s2 = stack.pop()
                s1 = stack.pop()
                match i:
                    case '+': res = s1 + s2
                    case '-': res = s1 - s2
                    case '*': res = s1 * s2
                    case '/': res = s1 / s2
                stack.append(int(res))
        return stack[-1]