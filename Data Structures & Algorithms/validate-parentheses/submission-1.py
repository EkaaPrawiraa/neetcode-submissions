class Solution:
    def isValid(self, s: str) -> bool:
        parent = {
            '}' : '{',
            ')' : '(',
            ']' : '[',
        }
        stack = []
        for char in s:
            if char in parent:
                if stack and stack[-1] == parent[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        