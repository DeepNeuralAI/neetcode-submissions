class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        res = []
        newInterval = intervals[0]
        res.append(newInterval)

        for i in range(1, len(intervals)):
            if intervals[i][0] <= newInterval[1]:
                min_start = min(intervals[i][0], newInterval[0])
                max_end = max(intervals[i][1], newInterval[1])
                newInterval[0] = min_start
                newInterval[1] = max_end
            else:
                newInterval = intervals[i]
                res.append(newInterval)
        
        return res

        