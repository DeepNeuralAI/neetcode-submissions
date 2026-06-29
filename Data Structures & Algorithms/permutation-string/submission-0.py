class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        expected = defaultdict(int)
        for c in s1:
            expected[c] += 1
        actual = defaultdict(int)
        
        for i in range(len(s1)):
            actual[s2[i]] += 1
        
        if actual == expected:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            actual[s2[l]] -= 1

            if actual[s2[l]] == 0:
                del actual[s2[l]]
            l += 1
            
            actual[s2[r]] += 1

            if actual == expected:
                return True
        
        return False
            
        