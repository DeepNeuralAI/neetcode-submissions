class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        
        stack = []
        for c in s:
            if c not in mapping:
                stack.append(c)
            else:
                if not stack:
                    return False
                
                if stack.pop() != mapping[c]:
                    return False
        
        return len(stack) == 0