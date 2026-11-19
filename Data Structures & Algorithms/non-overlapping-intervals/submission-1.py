class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        res = []

        count = 1
        s1, e1 = intervals[0]

        for i in range(1, len(intervals)):
            s2, e2 = intervals[i]

            if s2 >= e1:
                count += 1
                s1, e1 = intervals[i]
        
        return len(intervals) - count



        