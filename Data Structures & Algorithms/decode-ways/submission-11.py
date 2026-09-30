class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization

        def num_ways(s, start, memo):
            if start == len(s):
                return 1

            if s[start] == '0':
                return 0
            
            if start in memo:
                return memo[start]

            total = 0
            total += num_ways(s, start + 1, memo)

            two_digits = int(s[start : start + 2])
            if 10 <= two_digits <= 26:
                total += num_ways(s, start + 2, memo)
            
            memo[start] = total
            return total
        
        return num_ways(s, 0, {})

        