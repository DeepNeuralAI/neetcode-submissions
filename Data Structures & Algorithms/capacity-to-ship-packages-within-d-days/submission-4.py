class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        while l <= r:
            m = (l + r) // 2
            if self.get_days(weights, m) <= days:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
    

    def get_days(self, weights, capacity):
        num_days = 0
        current_weight = 0

        for w in weights:
            if current_weight + w <= capacity:
                current_weight += w
            else:
                num_days += 1
                current_weight = w
        
        if current_weight > 0:
            num_days += 1
        
        return num_days


        