class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        
        matchsticks.sort(reverse = True)
        
        target_length = total // 4
        sides = [target_length] * 4

        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(len(sides)):
                if sides[j] >= matchsticks[i]:
                    sides[j] -= matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[j] += matchsticks[i]
            return False
        
        return backtrack(0)
        