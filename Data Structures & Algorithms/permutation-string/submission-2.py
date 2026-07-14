class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        # Brute Force
        n = len(s2)
        m = len(s1)

        candidate = sorted(s1)
        
        for i in range(n - m + 1):
            subStr = s2[i : i + m]
            if sorted(subStr) == candidate:
                return True
        return False

            
        
        

        