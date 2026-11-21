class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        modified_q = [(q, i) for i, q in enumerate(queries)]
        modified_q.sort(key = lambda x: x[0])
        intervals.sort()
        heap = []
        res = [-1] * len(queries)
        k = 0

        for q, i in modified_q:
            while k < len(intervals) and intervals[k][1] < q:
                k += 1
            
            while k < len(intervals) and intervals[k][0] <= q:
                s, e = intervals[k]
                heapq.heappush(heap, (e - s + 1, e))
                k += 1
            
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            if heap:
                res[i] = heap[0][0]
        

        return res
        