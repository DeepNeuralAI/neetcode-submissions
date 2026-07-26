class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        count = defaultdict(int)
        window = defaultdict(int)

        for i in range(len(s1)):
            count[s1[i]] += 1
            window[s2[i]] += 1
        
        num_conditions = len(count)
        num_met = 0

        for c, freq in count.items():
            if freq == window.get(c, 0):
                num_met += 1
        
        if num_met == num_conditions:
            return True
        
        start = len(s1)
        end = len(s2)

        l = 0
        r = start

        while r < end:
            window[s2[r]] += 1

            if s2[r] in count:
                if window[s2[r]] - 1 == count[s2[r]]:
                    num_met -= 1
                elif window[s2[r]] == count[s2[r]]:
                    num_met += 1
            
            window[s2[l]] -= 1

            if s2[l] in count:
                if window[s2[l]] + 1 == count[s2[l]]:
                    num_met -= 1
                elif window[s2[l]] == count[s2[l]]:
                    num_met += 1
            
            if num_met == num_conditions:
                return True

            r += 1
            l += 1

        return False

        