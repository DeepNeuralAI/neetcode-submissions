class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        # Match Frequency
        n = len(s2)
        m = len(s1)

        count1 = defaultdict(int)
        
        for c in s1:
            count1[c] += 1
        
        for i in range(n - m + 1):
            count2 = defaultdict(int)
            for j in range(i, i + m):
                count2[s2[j]] += 1

            if count1 == count2:
                return True
        return False

            
        
        

        