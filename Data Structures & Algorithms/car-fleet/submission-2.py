class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        st = []

        for p, s in pair:
            time = (target - p) / s
            if st and st[-1] >= time:
                continue
            st.append(time)
        
        return len(st)
        