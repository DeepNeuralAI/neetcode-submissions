class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for op in tokens:
            if op == '+':
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif op == '-':
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif op == '*':
                first = stack.pop()
                second = stack.pop()
                stack.append(first * second)
            elif op == '/':
                divisor = stack.pop()
                dividend = stack.pop()
                stack.append(int(dividend / divisor))
            else:
                stack.append(int(op))
        
        return stack[0]