class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        
        tasks.sort(key = lambda t: t[0])
        minHeap, res = [], [] # (processing_time, task_id)
        i = time = 0

        while i < len(tasks) or minHeap:
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
           
            if minHeap:
                proc_time, task_id = heapq.heappop(minHeap)
                time += proc_time
                res.append(task_id)
            else:
                time = tasks[i][0]
        

        return res

            
            

        