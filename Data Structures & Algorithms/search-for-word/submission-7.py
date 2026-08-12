class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        if not word or not board:
            return True

        def search(r, c, i):
            if i == len(word):
                return True

            if not (0 <= r < ROWS and 0 <= c < COLS):
                return False
            
            if board[r][c] != word[i]:
                return False
            
            visited.add((r, c))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r_, c_ = r + dr, c + dc

                if (r_, c_) not in visited:
                    if search(r_, c_, i + 1):
                        return True

            visited.remove((r, c))

            return False


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != word[0]:
                    continue
                if search(r, c, 0):
                    return True
        return False
    


        