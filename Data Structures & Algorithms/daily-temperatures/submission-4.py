class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        stack = []

        for i in range(n):
            while stack and stack[-1][1] < temperatures[i]:
                day_idx, prev_temp = stack.pop()
                res[day_idx] = i - day_idx
            
            stack.append((i, temperatures[i]))
        
        return res

                

        