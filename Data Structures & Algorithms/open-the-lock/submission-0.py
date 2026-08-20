from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        
        if '0000' in deadends:
            return -1

        def bfs():
            queue = deque([('0000', 0)])
            visited.add('0000')

            while queue:
                state, d = queue.popleft()

                if state == target:
                    return d

                neighbors = self.get_neighbors(state)

                for adj in neighbors:
                    if adj in deadends or adj in visited:
                        continue
                    
                    visited.add(adj)
                    queue.append((adj, d + 1))
        
            return -1
        
        return bfs()
                
        
    def get_neighbors(self, state):
        digits = list(state)
        states = []

        for i in range(len(digits)):
            digit = int(digits[i])
            pos_digit = (digit + 1) % 10
            neg_digit = (digit - 1) % 10

            # +1
            digits[i] = str(pos_digit)
            states.append(''.join(digits))

            # -1
            digits[i] = str(neg_digit)
            states.append(''.join(digits))

            digits[i] = str(digit)

        return states




            
            

            