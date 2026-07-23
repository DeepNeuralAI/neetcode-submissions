class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                exists = True
            
                while stack and stack[-1] > 0 and a < 0:
                    diff = stack[-1] + a

                    if diff < 0:
                        stack.pop()
                    elif diff == 0:
                        stack.pop()
                        exists = False
                        break
                    else:
                        exists = False
                        break
            
                if exists:
                    stack.append(a)
        return stack



                

                    

                

        