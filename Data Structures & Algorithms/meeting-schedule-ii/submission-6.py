"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        
        arrivals = sorted([interval.start for interval in intervals])
        departures = sorted([interval.end for interval in intervals])
        i = j = 0
        cnt = maxCnt = 0
        n = len(intervals)


        while i < n and j < n:
            if arrivals[i] < departures[j]:
                cnt += 1
                i += 1
            else:
                cnt -=1
                j += 1
            
            maxCnt = max(maxCnt, cnt)
        
        return maxCnt



        

        