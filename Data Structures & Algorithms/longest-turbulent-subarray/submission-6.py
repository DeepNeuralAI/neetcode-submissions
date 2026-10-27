class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        up = [1] * n
        down = [1] * n

        res = 1

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up[i] = 1 + down[i - 1]
                down[i] = 1
            elif arr[i] < arr[i - 1]:
                down[i] = 1 + up[i - 1]
                up[i] = 1
            else:
                continue
            
            res = max(up[i], down[i], res)

        
        return res
