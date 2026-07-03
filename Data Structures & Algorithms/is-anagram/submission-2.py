class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        n = len(s)
        countT, countS = defaultdict(int), defaultdict(int)
        for i in range(n):
            countS[s[i]] += 1
            countT[t[i]] += 1
        

        for k, v in countT.items():
            if v != countS[k]:
                return False
        
        return True

        