import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search on answer space
        l = 1
        r = res = max(piles)

        def isValid(piles, rate):
            hours = 0
            for p in piles:
                hours += math.ceil(p / rate)
            
            return hours

        
        while l <= r:
            rate = (l + r) // 2
            if isValid(piles, rate) <= h:
                res = rate
                r = rate - 1
            else:
                l = rate + 1
        
        return res


        