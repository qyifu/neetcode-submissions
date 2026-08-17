class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        pair = {')': '(', ']':'[', '}':'{'}
        stack = []
        for char in s:
            if char in pair.values():
                stack.append(char)
            else:
                if stack and stack[-1] == pair[char]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

