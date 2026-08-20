class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if n != m:
            return False
        
        countS = defaultdict(int)
        countT = defaultdict(int)

        for i in range(n):
            countS[s[i]] += 1
            countT[t[i]] += 1
        
        return countS == countT

        