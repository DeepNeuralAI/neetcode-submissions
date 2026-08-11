class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr, res = [], []

        def backtrack(openCount, closedCount):

            if openCount == closedCount == n:
                res.append(''.join(curr))
                return
    
            # if openCount < n - can choose open
            if openCount < n:
                curr.append('(')
                backtrack(openCount + 1, closedCount)
                curr.pop()

            # if openCount > closedCount - can choose close

            if openCount > closedCount:
                curr.append(')')
                backtrack(openCount, closedCount + 1)
                curr.pop()
        
        backtrack(0, 0)
        return res
        