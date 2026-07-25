class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                curr = []
                while stack and stack[-1] != '[':
                    curr.append(stack.pop())

                curr.reverse()
                curr = ''.join(curr)
                
                stack.pop()

                number = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop()
                    number = digit + number
                
                number = int(number)
                stack.append(number * curr)
        
        return ''.join(stack)


        