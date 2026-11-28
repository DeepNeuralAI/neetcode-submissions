class Solution:
    def minEnd(self, n: int, x: int) -> int:
        target = n - 1

        i_x = i_n = 0
        res = x

        while target:
            mask = 1 << i_x
            
            if (mask & x):
                i_x += 1
                continue
            
            digit = target & 1
            target = target >> 1
            
            if digit:
                res = res | mask
            i_x += 1

        return res
            
            
            

            

        