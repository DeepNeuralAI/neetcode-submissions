class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        curr = ""
        for c in s:
            curr = ""
            
            if c == ']':
                while stack and stack[-1] != '[':
                    curr = stack.pop() + curr
                
                if stack: stack.pop()

                number = ""
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                
                if number:
                    number = int(number)
                    stack.append(curr * number)
            else:
                stack.append(c)
        
        return ''.join(stack)



        