from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        if s[-1] == '1':
            return False
        
        # Greedy
        q = deque([0])
        visited = set([0])

        while q:
            i = q.popleft()
            if i == n - 1:
                return True
            
            start = i + minJump
            end = min(i + maxJump + 1, n)

            for j in range(start, end):
                if s[j] == '0' and j not in visited:
                    visited.add(j)
                    q.append(j)
        
        return False
        


    
                
            
            


        