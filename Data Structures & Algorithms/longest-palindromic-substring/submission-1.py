class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Two Pointers - Expand from Middle
        # Treat each character as middle and expand outwards
        # This will not work for even length strings like "bb" - edge case

        resLen = 0
        res_start = res_end = None

        for i in range(len(s)):
            # odd length
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) >= resLen:
                    resLen = r - l + 1
                    res_start = l
                    res_end = r
                
                l -= 1
                r += 1
            
            
            # even length
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res_start = l
                    res_end = r
                
                l -= 1
                r += 1
        
        return s[res_start : res_end + 1]
     
            
                    
                    
                    


        