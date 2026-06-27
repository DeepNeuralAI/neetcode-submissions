class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Brute Force
        n = len(s)
        for i in range(n):
            new_s = ''
            for j in range(n):
                if i != j:
                    new_s += s[j]
            
            if self.isPalindrome(new_s):
                return True
        
        return False
    


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
            