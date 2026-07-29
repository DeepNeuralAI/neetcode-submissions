import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return s
        
        prev = None
        frequency_map = defaultdict(int)

        for c in s:
            frequency_map[c] += 1
        
        max_heap = [(-cnt, c) for c, cnt in frequency_map.items()]
        heapq.heapify(max_heap)
        res = []

        """
        heap = []
        prev = None
        res = [y, a, x, y]
        """

        while max_heap or prev:
            if prev and not max_heap:
                return ""

            cnt, c = heapq.heappop(max_heap)
            res.append(c)
            cnt += 1

            new_prev = (cnt, c) if cnt < 0 else None
        
            if prev:
                heapq.heappush(max_heap, prev)

            prev = new_prev
            
        return ''.join(res)

