class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '.':
                    continue
                
                sq_no = (r // 3) * 3 + (c // 3) 
                value = board[r][c]

                if value in rows[r]:
                    return False
                
                rows[r].add(value)
                
                if value in cols[c]:
                    return False
                
                cols[c].add(value)
                
                if value in squares[sq_no]:
                    return False
                
                squares[sq_no].add(value)
                
        return True

        