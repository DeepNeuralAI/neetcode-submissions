class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums, target):
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        

        ROWS, COLS = len(matrix), len(matrix[0])
        l = 0
        r = ROWS - 1

        while l <= r:
            m = (l + r) // 2
            selected_row = matrix[m]

            start, end = selected_row[0], selected_row[COLS - 1]
            if start <= target <= end:
                found = search(selected_row, target)
                return True if found != -1 else False
                    
            if target > end:
                l = m + 1
            else:
                r = m - 1
        
        return False
