class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_index_map = dict()

        l = r = 0
        n = len(s)
        res = 0

        while r < n:
            if s[r] in char_to_index_map and char_to_index_map[s[r]] >= l:
                l = char_to_index_map[s[r]] + 1
            
            char_to_index_map[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        
        return res