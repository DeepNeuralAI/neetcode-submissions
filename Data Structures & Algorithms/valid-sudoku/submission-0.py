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
        

        for i in range(0, ROWS, 3):
            for j in range(0, COLS, 3):
                visited = [False] * 9
                for r in range(3):
                    for c in range(3):
                        value = board[i + r][j + c]
                        if value == '.': continue
                        if visited[int(value) - 1]:
                            return False
                        visited[int(value) - 1] = True
        
        return True

                        



        