class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        """
        -2 -1 1 2 
        """
        for a in asteroids:
            if a < 0:
                exists = True
                # Destroy all smaller asteroids
                while stack and stack[-1] > 0 and abs(a) > stack[-1]:
                    stack.pop()
                
                # If remaining asteroid is equal
                if stack and stack[-1] == abs(a):
                    stack.pop()
                    exists = False
                
                if stack and stack[-1] > 0:
                    exists = False 
                
                if exists:
                    stack.append(a)

            else:
                stack.append(a)

        return stack