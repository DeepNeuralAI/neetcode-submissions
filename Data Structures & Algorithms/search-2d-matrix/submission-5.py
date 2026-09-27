class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l = 0
        r = ROWS - 1

        while l <= r:
            m = (l + r) // 2
            nums = matrix[m]

            l_bound = nums[0]
            r_bound = nums[COLS - 1]

            if l_bound <= target <= r_bound:
                col_idx = self.binary_search(nums, target)
                
                if col_idx != -1:
                    return True
                return False
            elif target > r_bound:
                l = m + 1
            else:
                r = m - 1
        
        return False

    
    
    def binary_search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            candidate = nums[m]

            if candidate == target:
                return m
            
            if candidate < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1

        