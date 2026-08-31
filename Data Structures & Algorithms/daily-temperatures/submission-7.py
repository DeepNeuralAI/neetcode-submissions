class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []


        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_idx, prev_tmp = stack.pop()
                res[prev_idx] = i - prev_idx
            
            stack.append((i, temp))
        
        return res

