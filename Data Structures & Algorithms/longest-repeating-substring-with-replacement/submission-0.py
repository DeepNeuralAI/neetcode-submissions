class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = 0
        res = 0

        count = defaultdict(int)

        while r < n:
            count[s[r]] += 1

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            if (r - l + 1) - max(count.values()) <= k:
                res = max(res, r - l + 1)
            
            r += 1
        return res





        