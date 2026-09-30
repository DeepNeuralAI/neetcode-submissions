class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Memoization
        def num_coins(coins, i, amount, memo):
            if amount == 0:
                return 0

            if i == len(coins) or amount < 0:
                return float('inf')

            if (i, amount) in memo:
                return memo[(i, amount)]
            
            take = float('inf')
            if coins[i] <= amount:
                take = 1 + num_coins(coins, i, amount - coins[i], memo)

            skip = num_coins(coins, i + 1, amount, memo)
            memo[(i, amount)] = min(take, skip)
            return memo[(i, amount)]

        res = num_coins(coins, 0, amount, {})
        return -1 if res == float('inf') else res

        