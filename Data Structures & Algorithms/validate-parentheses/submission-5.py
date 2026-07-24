class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        mapping = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        stack = []

        for bracket in s:
            if bracket in mapping:
                if not stack or stack[-1] != mapping[bracket]: return False
                stack.pop()
            else:
                stack.append(bracket)
    
        return len(stack) == 0
        