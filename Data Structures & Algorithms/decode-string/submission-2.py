class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        curr = ""
        for c in s:
            curr = ""
            
            if c == ']':
                while stack and stack[-1] != '[':
                    curr = stack.pop() + curr
                
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
            
                stack.append(curr * int(k))
            else:
                stack.append(c)
        
        return ''.join(stack)



        