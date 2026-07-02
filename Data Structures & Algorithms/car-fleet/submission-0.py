class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort()

        stack = []
        initial_time = (target - pair[0][0]) / pair[0][1]
        stack.append(initial_time)

        for p, s in pair[1:]:
            cur_time = (target - p) / s

            while stack and stack[-1] <= cur_time:
                stack.pop()

            stack.append(cur_time)

        return len(stack) 

        