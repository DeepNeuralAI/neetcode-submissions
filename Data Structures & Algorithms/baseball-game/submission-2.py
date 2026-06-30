class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        total = 0
        for op in operations:
            if op == '+':
                value = int(res[-1] + res[-2])
                total += value
                res.append(value)
            elif op == 'C':
                total -= res[-1]
                res.pop()
            elif op == 'D':
                value = 2 * res[-1]
                total += value
                res.append(value)
            else:
                value = int(op)
                total += value
                res.append(value)
        return total

            
        