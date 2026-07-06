class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS, self.COLS = len(matrix), len(matrix[0])
        self.prefix = [[0] * (self.COLS + 1) for _ in range(self.ROWS + 1)]
 
        for r in range(1, self.ROWS + 1):
            for c in range(1, self.COLS + 1):
                 self.prefix[r][c] = (self.prefix[r - 1][c] + 
                                      self.prefix[r][c - 1] -
                                      self.prefix[r - 1][c - 1] +
                                      matrix[r - 1][c - 1])
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1 = row1 + 1, col1 + 1
        r2, c2= row2 + 1, col2 + 1
        
        topLeft = self.prefix[r1 - 1][c1 - 1]
        curSum = self.prefix[r2][c2]

        topRight = self.prefix[r1 - 1][c2]
        bottomLeft = self.prefix[r2][c1 - 1]
        return curSum - topRight - bottomLeft + topLeft
    
   


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)