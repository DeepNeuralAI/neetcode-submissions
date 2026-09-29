class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return max(0, nums[0])

        first_config = self.max_profit(nums[:-1])
        second_config = self.max_profit(nums[1:])

        return max(first_config, second_config)
    

    def max_profit(self, houses):
        n = len(houses)
        if not houses:
            return 0
        
        if len(houses) == 1:
            return max(0, houses[0])
        
        profit = [0] * n
        profit[0] = houses[0]

        for i in range(1, len(houses)):
            profit[i] = houses[i] + profit[i - 2] if i - 2 >= 0 else houses[i]
            profit[i] = max(profit[i], profit[i - 1])
        
        return profit[n - 1]
            

        