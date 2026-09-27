import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)

        l = 1
        r = max_rate
        res = max_rate

        while l <= r:
            m = (l + r) // 2

            if self.get_hours(piles, m) <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
    
    def get_hours(self, piles, rate):
        num_hours = 0
        for bananas in piles:
            num_hours += math.ceil(bananas / rate)
        return num_hours

        