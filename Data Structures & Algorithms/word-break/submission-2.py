class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}

        def backtrack(i):
            if i == len(s):
                return True
            
            if i in memo:
                return memo[i]
            
            for end in range(i, len(s)):
                if s[i : end + 1] in wordDict:
                    if backtrack(end + 1):
                        memo[i] = True
                        return memo[i]
            
            memo[i] = False
            return memo[i]
        
        return backtrack(0)
        