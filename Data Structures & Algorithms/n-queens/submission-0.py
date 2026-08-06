class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        pos_diagonals = set()
        neg_diagonals = set()


        def backtrack(i):
            if i == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
            
            for c in range(n):
                if (c in cols or 
                    (i + c) in pos_diagonals or
                    (i - c) in neg_diagonals):
                    continue
                
                cols.add(c)
                pos_diagonals.add(i + c)
                neg_diagonals.add(i - c)
                board[i][c] = 'Q'

                backtrack(i + 1)

                cols.remove(c)
                pos_diagonals.remove(i + c)
                neg_diagonals.remove(i - c)
                board[i][c] = '.'

        backtrack(0)
        return res



        