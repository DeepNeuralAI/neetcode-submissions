class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                curr = ""
                while stack and stack[-1] != '[':
                    curr = stack.pop() + curr
                
                stack.pop()
                size = ""
                while stack and stack[-1].isdigit():
                    size = stack.pop() + size
                
                stack.append(int(size) * curr)
        
        return ''.join(stack)

