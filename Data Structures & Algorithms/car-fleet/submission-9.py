class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse = True) # Descending order of position (last ones first)

        stack = []
        for p, s in pairs:
            time_to_target = (target - p) / s
            stack.append(time_to_target)
           
            if len(stack) > 1:
                first = stack[-1]
                second = stack[-2]

                if first <= second:
                    stack.pop()
        
        return len(stack)
        

        # (p, s) -> (1, 3), (4, 2)
        # Sorted Desc: (4, 2), (1, 3)
        
        # time to target:
        # 3 seconds
        
        
        # Stack:
        # [3, 3]

        