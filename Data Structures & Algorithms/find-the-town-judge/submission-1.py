class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Town Judge would have no outgoing degrees
        # Town Judge would also have n - 1 incoming degrees
        
        indegrees = [0] * (1 + n)
        outdegrees = [0] * (1 + n)
        for src, dst in trust:
            outdegrees[src] += 1
            indegrees[dst] += 1


        for node in range(1, n + 1):
            if indegrees[node] == n - 1 and outdegrees[node] == 0:
                return node

        return -1
        