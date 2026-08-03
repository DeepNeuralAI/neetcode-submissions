class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.solve([], res, 0, 0, n)
        return res


    def solve(self, current, res, openCount, closedCount, n):
        if openCount == n and closedCount == n:
            res.append(''.join(current))
            return
        
        if openCount < n:
            current.append('(')
            self.solve(current, res, openCount + 1, closedCount, n)
            current.pop()

        if openCount > closedCount:
            current.append(')')
            self.solve(current, res, openCount, closedCount + 1, n)
            current.pop()
        


        