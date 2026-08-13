class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos_diagonals = set()
        neg_diagonals = set()

        board = [['.'] * n for _ in range(n)]
        res = []
    
        def backtrack(row):
            if row == n:
                return 1
            
            num_ways = 0
            for col in range(n):
                if isSafe(row, col):
                    cols.add(col)
                    pos_diagonals.add(row + col)
                    neg_diagonals.add(row - col)
                    
                    num_ways += backtrack(row + 1)

                    cols.remove(col)
                    pos_diagonals.remove(row + col)
                    neg_diagonals.remove(row - col)
            
            return num_ways
            

        def isSafe(r, c):
            if c in cols:
                return False
            
            if (r + c) in pos_diagonals:
                return False
            
            if (r - c) in neg_diagonals:
                return False
            
            return True
        
        return backtrack(0)
        
        
    
    def board_to_string(self, board):
        return [''.join(row) for row in board]
 