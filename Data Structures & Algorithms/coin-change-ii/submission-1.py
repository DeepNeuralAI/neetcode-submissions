class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def ways(i, target, memo):
            if target == 0:
                return 1
            
            if i == len(coins) or amount < 0:
                return 0
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            c1 = 0
            if target - coins[i] >= 0:
                c1 = ways(i, target - coins[i], memo)
            
            c2 = ways(i + 1, target, memo)
            memo[(i, target)] = c1 + c2
            return memo[(i, target)]
        
        return ways(0, amount, {})
        

        
        