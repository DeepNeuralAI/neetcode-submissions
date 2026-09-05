class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count = defaultdict(int)
        window = defaultdict(int)
        
        for i in range(len(s1)):
            count[s1[i]] += 1
            window[s2[i]] += 1
        
        num_conditions_required = len(count)
        num_conditions_met = 0
        
        for c in window:
            if window[c] == count.get(c, 0):
                num_conditions_met += 1
        
        if num_conditions_met == num_conditions_required:
            return True

        r = len(s1)
        l = 0
        while r < len(s2):
            window[s2[r]] += 1

            if window[s2[r]] == count.get(s2[r]):
                num_conditions_met += 1
            elif window[s2[r]] - 1  == count.get(s2[r]):
                num_conditions_met -= 1
            
            window[s2[l]] -= 1
            if window[s2[l]] + 1 == count.get(s2[l]):
                    num_conditions_met -= 1
            elif window[s2[l]] == count.get(s2[l]):
                    num_conditions_met += 1
            
            if num_conditions_met == num_conditions_required:
                return True
            
            l += 1
            r += 1
        return False



