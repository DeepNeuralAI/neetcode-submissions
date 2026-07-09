class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        mapping = {
            ')' : '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for c in s:
            if c not in mapping:
                stack.append(c)
            elif not stack or stack[-1] != mapping[c]:
                return False
            else:
                stack.pop()
        
        return len(stack) == 0