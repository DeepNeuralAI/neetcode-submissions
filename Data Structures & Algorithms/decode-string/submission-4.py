class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        # stack = 2, [, a, 3, [, b
        # stack = abbbabbb, c

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                string = ""
                while stack and stack[-1].isalpha():
                    char = stack.pop()
                    string = char + string
                
                stack.pop()
                number = ""
                while stack and stack[-1].isdigit():
                    char = stack.pop()
                    number = char + number
                
                freq = int(number)
                stack.append(freq * string)
        
        return ''.join(stack)
                



        