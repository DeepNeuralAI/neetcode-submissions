class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            if not self.isRowValid(board[r]):
                return False
        
        for c in range(COLS):
            if not self.isColValid(board, c):
                return False
            
        for i in range(9):
            row = (i // 3) * 3
            col = (i % 3) * 3

            if not self.isSquareValid(board, row, col):
                return False
        
        return True

    
    def isColValid(self, board, col):
        ROWS, COLS = len(board), len(board[0])
        expected = set(str(n) for n in range(1, 10))
        
        for r in range(ROWS):
            if board[r][col] == ".":
                continue
            if board[r][col] in expected:
                expected.remove(board[r][col])
            else:
                return False
        return True


    def isRowValid(self, row):
        expected = set(str(n) for n in range(1, 10))

        for r in row:
            if r == '.': continue
            
            if r in expected:
                expected.remove(r)
            else:
                return False
        return True
    
    def isSquareValid(self, board, r, c):
        expected = set(str(n) for n in range(1, 10))
        
        for i in range(3):
            for j in range(3):
                if board[r + i][c + j] == '.': continue 
                
                if board[r + i][c + j] in expected:
                    expected.remove(board[r + i][c + j])
                else:
                    return False
        return True

        