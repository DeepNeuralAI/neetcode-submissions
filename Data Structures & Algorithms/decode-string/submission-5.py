class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ']':
                string = ""
                while stack and stack[-1] != '[':
                    char = stack.pop()
                    string = char + string
                
                stack.pop()
                
                length = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop()
                    length = digit + length
                
                stack.append(int(length) * string)
            else:
                stack.append(c)
        
        return ''.join(stack)
                


        