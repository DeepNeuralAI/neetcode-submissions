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
        ships = 1
        cur_weight = capacity
        
        for w in weights:
            if cur_weight - w < 0:
                ships += 1
                cur_weight = capacity
                
            cur_weight -= w
        return ships

