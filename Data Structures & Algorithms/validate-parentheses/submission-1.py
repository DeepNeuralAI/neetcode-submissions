class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ']': '[',
            '}': '{',
            ')': '('

        }
        stack = []

        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif stack and mapping[c] == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
        
        