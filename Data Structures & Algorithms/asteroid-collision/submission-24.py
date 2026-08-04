class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        """
        -2 -1 1 2 
        """
        for a in asteroids:
            if a < 0:
                exists = True
                while stack and stack[-1] > 0:
                    diff = stack[-1] + a
                    
                    if diff > 0:
                        exists = False
                        break
                    elif diff < 0:
                        stack.pop()
                        continue
                    else:
                        stack.pop()
                        exists = False
                        break
                
                if exists:
                    stack.append(a)
            else:
                stack.append(a)
        return stack

             