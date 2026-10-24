class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.ROWS, self.COLS = len(board), len(board[0])
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(self.ROWS):
            for c in range(self.COLS):
                digit = board[r][c]

                if digit == '.':
                    continue
    
                sq_no = self.get_square_number(r, c)

                if (digit in rows[r] 
                    or digit in cols[c]
                    or digit in squares[sq_no]):
                    return False
                
                rows[r].add(digit)
                cols[c].add(digit)
                squares[sq_no].add(digit)

        return True

    def get_square_number(self, r, c):
        return 3 * (r // 3) + (c // 3)
        