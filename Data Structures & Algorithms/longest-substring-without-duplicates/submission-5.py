class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute Force
        n = len(s)
        maxLen = 0
        
        for i in range(n):
            seen = set()
            length = 0
            for j in range(i, n):
                if s[j] not in seen:
                    seen.add(s[j])
                    length += 1
                    maxLen = max(maxLen, length)
                else:
                    break
        return maxLen


