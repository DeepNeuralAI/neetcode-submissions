class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(int)
        window = defaultdict(int)

        for c in t:
            countT[c] += 1
        
        num_conditions = len(countT)
        num_met = 0

        l = r = 0
        res = ""
        res_len = float('inf')

        while r < len(s):
            window[s[r]] += 1

            if s[r] in countT and countT[s[r]] == window[s[r]]:
                num_met += 1
            
            while num_met == num_conditions:
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = s[l:r+1]

                if s[l] in countT and window[s[l]] == countT[s[l]]:
                    num_met -= 1
                
                window[s[l]] -= 1
                l += 1
            r += 1
        
        return res
