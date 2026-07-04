class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Staircase Method
        ROWS, COLS = len(matrix), len(matrix[0])
        r = 0
        c = COLS - 1

        while r < ROWS and c >= 0:
            if matrix[r][c] == target:
                return True
            
            if matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        return False