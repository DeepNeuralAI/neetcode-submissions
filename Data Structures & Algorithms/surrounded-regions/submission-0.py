class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visit = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(node):
            r, c = node
            if board[r][c] != 'O':
                return

            visit.add(node)

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r_ = r + dr
                c_ = c + dc

                if (not (0 <= r_ < ROWS and 0 <= c_ < COLS) 
                    or (r_, c_) in visit
                    or board[r_][c_] != 'O'):
                    continue
                
                dfs((r_, c_))
        
        for r in range(ROWS):
            dfs((r, 0))
            dfs((r, COLS - 1))
        
        for c in range(COLS):
            dfs((0, c))
            dfs((ROWS - 1, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r, c) not in visit:
                    board[r][c] = 'X'
        