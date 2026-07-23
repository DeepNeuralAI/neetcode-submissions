class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(a):
                    stack.pop()
                
                if stack and stack[-1] == abs(a):
                    stack.pop()
                elif stack and stack[-1] > 0:
                    continue
                else:
                    stack.append(a)
        return stack