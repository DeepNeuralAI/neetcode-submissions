class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(key = lambda x: x[0], reverse = True)
        n = len(pairs)

        stack = [] #(timeToDestination)

        for p, s in pairs:
            time_to_target = (target - p) / s
            stack.append((time_to_target))
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
        





        