class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profits = [(p, i) for i, p in enumerate(profits)]
        capital = [(c, i) for i, c in enumerate(capital)]

        i = 0
        n = len(capital)
        capital.sort()

        max_heap = []

        while i < n or max_heap:
            while i < n and capital[i][0] <= w:
                profit, idx = profits[capital[i][1]]
                heapq.heappush(max_heap, (-profit, idx))
                i += 1
            
            if not max_heap:
                return w
            
            profit, idx = heapq.heappop(max_heap)
            # w -= capital[idx][0]
            w -= profit
            
            k -= 1

            if k == 0:
                break
        
        return w
        






        