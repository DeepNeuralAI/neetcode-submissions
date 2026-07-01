class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in "+-/*":
                stack.append(int(tokens[i]))
                continue
            
            if tokens[i] == '+':
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif tokens[i] == '*':
                 stack.append(stack.pop() * stack.pop())     
            else:
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
        
        return stack.pop()

