class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0:
                heapq.heappush(heap, (count, char))

        res = []

        while heap:
            cnt, char = heapq.heappop(heap)
            
            if len(res) >= 2 and res[-1] == res[-2] == char:
                # Pop second most frequent
                if not heap:
                    break

                cnt2, char2 = heapq.heappop(heap)
                cnt2 += 1
                res.append(char2)
                
                if cnt2 != 0:
                    heapq.heappush(heap, (cnt2, char2))
                
                heapq.heappush(heap, (cnt, char))
            else:
                res.append(char)
                cnt += 1

                if cnt != 0:
                    heapq.heappush(heap, (cnt, char))
        return ''.join(res)