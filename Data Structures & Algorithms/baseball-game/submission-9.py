class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                first = stack[-1]
                second = stack[-2]
                stack.append(first + second)
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(op))
            
        return sum(stack)

        