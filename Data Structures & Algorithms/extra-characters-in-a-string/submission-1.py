class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        cache = {}

        def solve(i):
            if i == len(s):
                return 0
            
            if i in cache:
                return cache[i]
            
            res = 1 + solve(i + 1)
            
            for j in range(i, len(s)):
                if s[i : j + 1] in dictionary:
                    res = min(res, solve(j + 1))
            
            cache[i] = res
            return res
        
        return solve(0)





        