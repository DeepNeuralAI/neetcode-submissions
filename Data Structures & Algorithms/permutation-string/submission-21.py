class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count = defaultdict(int)
        
        for c in s1:
            count[c] += 1
        
        num_conditions_met = len(count)
        window = defaultdict(int)
        actual_conditions = 0

        l = r = 0
        while r < len(s2):
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1

                if window[s2[l]] + 1 == count.get(s2[l], 0):
                    actual_conditions -= 1
                
                if window[s2[l]] == count.get(s2[l], 0):
                    actual_conditions += 1
                
                l += 1
            
            window[s2[r]] += 1

            if window[s2[r]] == count.get(s2[r], 0):
                actual_conditions += 1
            
            if window[s2[r]] - 1  == count.get(s2[r], 0):
                actual_conditions -= 1
            
            if actual_conditions == num_conditions_met:
                return True
            
            r += 1
        return False



