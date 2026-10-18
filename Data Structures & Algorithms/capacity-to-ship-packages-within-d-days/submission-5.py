class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Binary Search on Answer Space
        l = max(weights)
        r = sum(weights)
        res = r

        def isValid(weights, capacity):
            days = 0
            currCap = 0
            for w in weights:
                currCap += w

                if currCap > capacity:
                    days += 1
                    currCap = w
            
            if currCap > 0:
                days += 1
            return days


        while l <= r:
            m = (l + r) // 2
            if isValid(weights, m) <= days:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

