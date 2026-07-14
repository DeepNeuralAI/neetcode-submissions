class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mpp = {}
        maxLen = 0

        l = r = 0

        while r < len(s):
            if s[r] not in mpp:
                mpp[s[r]] = r
            else:
                l = max(l, mpp[s[r]] + 1)
                mpp[s[r]] = r
            
            maxLen = max(maxLen, r - l + 1)
            r += 1
        
        return maxLen