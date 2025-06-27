class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""
        for i in range(len(s)):
            if s[i] == '(':
                stack += '('
            elif s[i] == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack = stack[:-1]
                else:
                    return False
            elif s[i] == '{':
                stack += '{'
            elif s[i] == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    stack = stack[:-1]
                else:
                    return False
            elif s[i] == '[':
                stack += '['
            elif s[i] == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack = stack[:-1]
                else:
                    return False
            else:
                return False
        return True if stack == "" else False