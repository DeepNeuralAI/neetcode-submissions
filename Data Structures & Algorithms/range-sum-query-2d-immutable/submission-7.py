class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        prefixSum = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                top = prefixSum[r - 1][c]
                left = prefixSum[r][c - 1]
                topLeft = prefixSum[r - 1][c - 1]

                prefixSum[r][c] = top + left - topLeft + matrix[r - 1][c - 1]
        
        self.prefixSum = prefixSum

        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1 = row1 + 1, col1 + 1
        r2, c2 = row2 + 1, col2 + 1

        topRight = self.prefixSum[r1 - 1][c2]
        bottomLeft = self.prefixSum[r2][c1 - 1]
        topLeft = self.prefixSum[r1 - 1][c1 - 1]
        res = self.prefixSum[r2][c2]

        return res + topLeft - topRight - bottomLeft

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)