class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            min_start = min(intervals[i][0], newInterval[0])
            max_end = max(intervals[i][1], newInterval[1])
            newInterval = [min_start, max_end]
            i += 1
        res.append(newInterval)

        while i < n and intervals[i][0] > newInterval[1]:
            res.append(intervals[i])
            i += 1
        
        return res


        
        
        
                
        