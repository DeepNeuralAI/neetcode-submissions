class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '.':
                    continue
                
                value = board[r][c]

                if (value in rows[r] or 
                   value in cols[c]):
                    return False
                
                sq_no = (r // 3) * 3 + (c // 3)
                
                if value in squares[sq_no]:
                    return False
                
                rows[r].add(value)
                cols[c].add(value)
                squares[sq_no].add(value)
        
        return True
                



