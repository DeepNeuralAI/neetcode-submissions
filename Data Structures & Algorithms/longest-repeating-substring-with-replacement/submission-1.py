class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = 0
        res = 0

        count = defaultdict(int)
        maxFreq = 0

        while r < n:
            count[s[r]] += 1
            maxFreq = max(maxFreq, count[s[r]])

            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            
            r += 1
        return res





        