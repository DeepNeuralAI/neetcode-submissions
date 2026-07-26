class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxLen = 0
        count = defaultdict(int)

        l = r = 0
        while r < n:
            count[s[r]] += 1
            
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen


        