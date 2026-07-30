class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)


        if not board:
            return True
        
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                cell = board[r][c]
                if cell == '.':
                    continue
                
                sq_id = (r // 3) * 3 + (c // 3)
                
                if (cell in rows[r] or 
                    cell in cols[c] or
                    cell in squares[sq_id]):
                    return False
                
                rows[r].add(cell)
                cols[c].add(cell)
                squares[sq_id].add(cell)
        
        return True
                


        