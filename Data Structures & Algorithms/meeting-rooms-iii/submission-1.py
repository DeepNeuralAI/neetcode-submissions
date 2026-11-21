class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        count = [0] * n
        available = [i for i in range(n)]
        used = []
        meetings.sort()


        for s, e in meetings:
            while used and used[0][0] <= s:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
            
            if available:
                room = heapq.heappop(available)
                heapq.heappush(used, (e, room))
                count[room] += 1
            else:
                next_free_time, room = heapq.heappop(used)
                heapq.heappush(used, (next_free_time + e - s, room))
                count[room] += 1
        
        max_cnt = max(count)
        return count.index(max_cnt)



        