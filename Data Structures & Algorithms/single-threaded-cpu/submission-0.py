class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        
        tasks.sort()
        minHeap = [] # (processing_time, task_id)
        time = 0
        i = 0
        order = []


        while i < len(tasks) or minHeap:
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2]))
                i += 1
           
            if minHeap:
                proc_time, task_id = heapq.heappop(minHeap)
                order.append(task_id)
                time += proc_time
            
            if not minHeap and i < len(tasks):
                time = max(time, tasks[i][0])
        

        return order

            
            

        