class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        # monotonically decreasing (from bottom - top)
        stack = [] # (prev_temp, day_idx)

        """
        [30, 38, 30, 26, 35, 40, 28]
        stack = [(40, 5), (28, 6)]
        result = [1, 4, 2, 1, 1, 0, 0] 
        """

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_temp, day_idx = stack.pop()
                result[day_idx] = i - day_idx
            
            stack.append((temp, i))
        
        return result