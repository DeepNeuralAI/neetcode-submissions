class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        if s[-1] == '1':
            return False
        
        # Bottom Up
        dp = [False] * n
        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            if s[i] == '1':
                continue
            
            start = i + minJump
            end = min(i + maxJump + 1, n)

            for j in range(start, end):
                if dp[j]:
                    dp[i] = True
                    break
                
        return dp[0]
                
            
            


        