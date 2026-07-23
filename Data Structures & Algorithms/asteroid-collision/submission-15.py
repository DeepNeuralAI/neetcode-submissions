class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            exists = True
            
            while stack and a < 0 and stack[-1] > 0 and exists:
                diff = stack[-1] + a

                if diff < 0:
                    stack.pop()
                elif diff == 0:
                    stack.pop()
                    exists = False
                else:
                    exists = False
            
            if exists:
                stack.append(a)
        return stack



                

                    

                

        