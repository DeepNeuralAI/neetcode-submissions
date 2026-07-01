class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n


        for i in range(n):
            while stack and temperatures[i] > stack[-1][0]:
                temp, j = stack.pop()
                res[j] = i - j
            
            stack.append((temperatures[i], i))
        
        return res
            
