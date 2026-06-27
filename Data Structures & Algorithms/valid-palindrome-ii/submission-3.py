class Solution:
    def validPalindrome(self, s: str) -> bool:
       n = len(s)
       l = 0
       r = n - 1
       
       while l < r:
            if s[l] != s[r]:
                skipL = s[l + 1: r + 1]
                skipR = s[l : r]

                if (not self.isPalindrome(skipL) and 
                    not self.isPalindrome(skipR)):
                    return False
            
            l += 1
            r -= 1
        
       return True

    def isPalindrome(self, s):
        n = len(s)
        i = 0
        j = n - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
            