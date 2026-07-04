class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        res = r
        while l <= r:
            m = (l + r) // 2

            if self.numDaysReq(weights, m) <= days:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
    
    def numDaysReq(self, weights, capacity):
        days = 1
        cur_weight = 0
        
        for w in weights:
            cur_weight += w

            if cur_weight > capacity:
                days += 1
                cur_weight = w
        return days
