class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            k = (l + r) // 2

            if self.numHours(piles, k) <= h:
                r = k
            else:
                l = k + 1
        
        return l
    

    def numHours(self, piles, k):
        time = 0
        for num in piles:
            time += math.ceil(num / k)
        return time
        