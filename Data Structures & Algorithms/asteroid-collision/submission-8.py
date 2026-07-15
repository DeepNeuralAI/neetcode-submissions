class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        

        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                is_destroyed = False
                while stack and stack[-1] > 0:
                    if abs(a) < stack[-1]:
                        is_destroyed = True
                        break
                    elif abs(a) == stack[-1]:
                        stack.pop()
                        is_destroyed = True
                        break
                    else:
                        stack.pop()
                
                if not is_destroyed:
                    stack.append(a)
        return stack