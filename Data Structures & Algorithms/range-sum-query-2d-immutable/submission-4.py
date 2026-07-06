class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS, self.COLS = len(matrix), len(matrix[0])
        self.prefix = [[0] * (self.COLS) for _ in range(self.ROWS)]
        self.prefix[0][0] = matrix[0][0]

        for c in range(1, self.COLS):
            self.prefix[0][c] = matrix[0][c] + self.prefix[0][c - 1]
        
        for r in range(1, self.ROWS):
            self.prefix[r][0] = matrix[r][0] + self.prefix[r - 1][0]
        
        for r in range(1, self.ROWS):
            for c in range(1, self.COLS):
                 self.prefix[r][c] = (self.prefix[r - 1][c] + self.prefix[r][c - 1] - self.prefix[r - 1][c - 1]) + matrix[r][c]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topLeft = self.prefix[row1 - 1][col1 - 1] if row1 - 1 >= 0 and col1 - 1 >= 0 else 0
        curSum = self.prefix[row2][col2]

        topRight = self.prefix[row1 - 1][col2] if row1 - 1 >= 0 else 0
        bottomLeft = self.prefix[row2][col1 - 1] if col1 - 1 >= 0 else 0
        return curSum - topRight - bottomLeft + topLeft
    
   


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)