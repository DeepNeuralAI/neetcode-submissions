class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                top = self.prefix[r - 1][c]
                left = self.prefix[r][c - 1]
                topLeft = self.prefix[r - 1][c - 1]
                self.prefix[r][c] = matrix[r - 1][c - 1] + top  + left - topLeft 
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.prefix[row1][col2 + 1]
        left = self.prefix[row2 + 1][col1]
        topLeft = self.prefix[row1][col1]

        return self.prefix[row2 + 1][col2 + 1] - top - left + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)