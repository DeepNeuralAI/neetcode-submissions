class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        squares = set()

        # (4, 3) -> square 4
        # (4, 6) -> square 5
        # (4, 3) -> (4 // 3) * 3 + (3 // 3)

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '.':
                    continue
                
                value = board[r][c]
                square_no = (r // 3) * 3 + (c // 3)
                
                if ((r, value) in rows or
                    (c, value) in cols or
                    (square_no, value) in squares):
                    return False
                
                rows.add((r, value))
                cols.add((c, value))
                squares.add((square_no, value))
        
        return True



        