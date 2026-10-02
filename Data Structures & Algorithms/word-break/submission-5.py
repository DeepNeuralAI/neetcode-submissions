class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Bottom Up
        # dp[i] is whether 0..i can be segmented in a valid form
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(dp)):
            for j in range(i - 1, -1, -1):
                if s[j : i] in wordDict and dp[j]:
                    dp[i] = True
        
        return dp[len(s)]


       