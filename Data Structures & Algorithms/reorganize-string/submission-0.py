class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = defaultdict(int)

        for c in s:
            freq[c] += 1
        
        heap = []
        res = []
        for c, count in freq.items():
            heapq.heappush(heap, (-count, c))
        
        prev = None
        while heap or prev:
            if not heap:
                return ""

            count, c = heapq.heappop(heap)
            res.append(c)

            count += 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None
            
            if count != 0:
                prev = (count, c)
        
        return ''.join(res)

            