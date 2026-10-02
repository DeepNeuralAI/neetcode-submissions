class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Bottom Up
        # dp[i] is whether 0..i can be segmented in a valid form
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        n = len(s)

        for i in range(n - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i : j + 1] in wordDict and dp[j + 1]:
                    dp[i] = True
                    break
        
        return dp[0]


       