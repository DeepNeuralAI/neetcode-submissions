class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        countT = defaultdict(int)

        for i in range(len(t)):
            countT[t[i]] += 1
        
        window = {}
        res, resLen = [-1, -1], float("infinity") 
        have, need = 0, len(countT)
        
        l = r = 0
        while r < len(s):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
            r += 1
        return s[res[0]: res[1] + 1] if resLen != float("infinity") else ""

    def isContained(self, s_map, t_map):
        for k, v in t_map.items():
            if s_map.get(k, 0) < v:
                return False
        
        return True