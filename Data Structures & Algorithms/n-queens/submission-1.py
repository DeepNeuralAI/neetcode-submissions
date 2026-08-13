class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diagonals = set()
        neg_diagonals = set()

        board = [['.'] * n for _ in range(n)]
        res = []
    
        def backtrack(row):
            if row == n:
                res.append(self.board_to_string(board))
                return
            
            for col in range(n):
                if isSafe(row, col):
                    cols.add(col)
                    pos_diagonals.add(row + col)
                    neg_diagonals.add(row - col)
                    
                    board[row][col] = 'Q'
                    backtrack(row + 1)

                    board[row][col] = '.'
                    cols.remove(col)
                    pos_diagonals.remove(row + col)
                    neg_diagonals.remove(row - col)
            

        def isSafe(r, c):
            if c in cols:
                return False
            
            if (r + c) in pos_diagonals:
                return False
            
            if (r - c) in neg_diagonals:
                return False
            
            return True
        
        backtrack(row = 0)
        return res
        
    
    def board_to_string(self, board):
        n = len(board)
        string_board = []
        for r in range(n):
            string_board.append(''.join(board[r]))
        return string_board




        
        
        