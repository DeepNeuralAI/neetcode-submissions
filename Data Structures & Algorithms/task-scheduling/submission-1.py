from heapq import heapify, heappop, heappush

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = defaultdict(int)
        for task in tasks:
            count[task] += 1
        
        heap = [(-cnt, task) for task, cnt in count.items()]
        heapq.heapify(heap)
        schedule = [] # (timeAvailable, count, task)
        time = 0

        # heap = []
        # schedule = []
        # time = 5

        # current

        while heap or schedule:
            while schedule and schedule[0][0] <= time:
                timeAvailable, count, task = heappop(schedule)
                heappush(heap, (count, task))

            if heap:
                count, task = heappop(heap)
                count += 1

                if count != 0:
                    heappush(schedule, (time + n + 1, count, task))
                
                time += 1
            
            if not heap and schedule:
                time = max(time, schedule[0][0])
        
        return time






        
        