from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Measure indegrees and outdegrees
        # Town judge would have 0 outdegrees and n - 1 indegrees

        indegrees = defaultdict(int)
        outdegrees = defaultdict(int)
        
        for src, dst in trust:
            outdegrees[src] += 1
            indegrees[dst] += 1
        
        for person in range(1, n + 1):
            if indegrees[person] == n - 1 and outdegrees[person] == 0:
                return person
        
        return -1

        