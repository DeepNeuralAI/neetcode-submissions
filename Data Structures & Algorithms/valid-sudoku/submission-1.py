class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        # Check All Rows
        for i in range(ROWS):
            visited = [False] * 9
            for j in range(COLS):
                value = board[i][j]
                if value == '.': 
                    continue
                if visited[int(value) - 1]:
                    return False
                visited[int(value) - 1] = True

        for c in range(COLS):
            visited = [False] * 9
            for r in range(ROWS):
                value = board[r][c]
                if value == '.': continue
                
                if visited[int(value) - 1]:
                    return False
                visited[int(value) - 1] = True
        

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j

                    if board[row][col] == '.':
                        continue
                    
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True

                        



        