class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Brute Force
        ROWS, COLS = len(matrix), len(matrix[0])

        l = 0
        r = ROWS - 1

        while l <= r:
            m = (l + r) // 2
            row = matrix[m]

            if row[0] <= target <= row[COLS - 1]:
                return self.search(row, target)
            
            if target < row[0]:
                r = m - 1
            elif target > row[COLS - 1]:
                l = m + 1
        
        return False

    

    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return True
            
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
        