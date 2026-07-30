class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        heap = []
        curCapacity = capacity

        for t in trips:
            curPassengers, start, end = t
            while heap and heap[0][0] <= start:
                prev_end, numPassengers = heapq.heappop(heap)
                curCapacity += numPassengers
            
            curCapacity -= curPassengers

            if curCapacity < 0:
                return False
            
            heapq.heappush(heap, (end, curPassengers))
        
        return True