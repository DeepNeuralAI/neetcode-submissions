class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                cell = board[r][c]
                
                if cell == '.':
                    continue
                
                s = (r // 3) * 3 + (c // 3)

                if (cell in cols[c] or 
                    cell in rows[r] or 
                    cell in squares[s]):
                        return False
                
                cols[c].add(cell)
                rows[r].add(cell)
                squares[s].add(cell)

        return True
        