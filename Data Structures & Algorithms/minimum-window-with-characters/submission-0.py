class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        countS = defaultdict(int)
        countT = defaultdict(int)

        for i in range(len(t)):
            countT[t[i]] += 1
        
        res, resLen = [-1, -1], float("infinity") 
        l = r = 0

        while r < len(s):
            countS[s[r]] += 1

            while self.isContained(countS, countT):
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                countS[s[l]] -= 1
                l += 1
            r += 1
        return s[res[0]: res[1] + 1] if resLen != float("infinity") else ""

    def isContained(self, s_map, t_map):
        for k, v in t_map.items():
            if s_map.get(k, 0) < v:
                return False
        
        return True