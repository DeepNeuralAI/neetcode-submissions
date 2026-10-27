class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)

        def up(i, memo, down_memo):
            if i == 0:
                return 1
            
            if i in memo:
                return memo[i]
            
            if arr[i] > arr[i - 1]:
                memo[i] = down(i - 1, down_memo, memo) + 1
                return memo[i]
    
            memo[i] = 1
            return 1


        def down(i, memo, up_memo):
            if i == 0:
                return 1
            
            if i in memo:
                return memo[i]
            
            if arr[i - 1] > arr[i]:
                memo[i] = 1 + up(i - 1, up_memo, memo)
                return memo[i]
            
            memo[i] = 1
            return 1
        
        up_memo = {0: 1}
        down_memo = {0: 1}

        up(n - 1, up_memo, down_memo)
        down(n - 1, down_memo, up_memo)

        res = 1

        for i in range(n):
            res = max(
                res,
                up(i, up_memo, down_memo),
                down(i, down_memo, up_memo)
            )

        return res
