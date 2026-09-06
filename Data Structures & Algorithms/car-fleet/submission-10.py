class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse = True) # Descending order of position (last ones first)

        stack = []
        for p, s in pairs:
            time_to_target = (target - p) / s

            if not stack or (stack[-1] < time_to_target):
                stack.append(time_to_target)
    
        return len(stack)
        

    #    position=[4,1,0,7]
    #    speed=[2,2,1,1]

       # (position, speed)
       # (7, 1), (4, 2), (1, 2), (0, 1)
       
       # time to target:



       # stack:
    #    [3, 4.5, 10]

        