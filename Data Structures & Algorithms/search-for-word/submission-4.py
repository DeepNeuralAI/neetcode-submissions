class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS, self.COLS = len(board), len(board[0])
        visited = set()

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == word[0]:
                    if self.solve(board, 0, r, c, visited, word):
                        return True
        return False
    
    
    def solve(self, board, idx, r, c, visited, word):
        if idx == len(word):
            return True
        

        if board[r][c] != word[idx]:
            return False

        if idx == len(word) - 1:
            return True
        
        visited.add((r, c))
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            r_ = r + dr 
            c_ = c + dc

            if self.isValid(r_, c_) and (r_, c_) not in visited:
                res = self.solve(board, idx + 1, r_, c_, visited, word)

                if res:
                    return True

        visited.remove((r, c))
        return False


    def isValid(self, r, c):
        return 0 <= r < self.ROWS and 0 <= c < self.COLS