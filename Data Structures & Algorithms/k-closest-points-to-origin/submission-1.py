class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x1, y1 in points:
            d = self.dist(x1, 0, y1, 0)
            heapq.heappush(heap, (-d, x1, y1))

            if len(heap) > k:
                heapq.heappop(heap)     
    
        res = []
        while k > 0:
            (d, x, y) = heapq.heappop(heap)
            res.append([x, y])
            k -= 1
        
        return res
        
    

    def dist(self, x1, x2, y1, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        