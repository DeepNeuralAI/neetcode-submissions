class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count = defaultdict(int)
        
        for c in s1:
            count[c] += 1
        
        # num_conditions = len(count)
        window = defaultdict(int)

        l = r = 0
        while r < len(s2):
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                
                l += 1
            
            window[s2[r]] += 1

            if window == count:
                return True

            r += 1
        return False



