class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        i_x = i_n = 1
        target = n - 1

        while i_n <= target:
            x_bit = i_x & x
            n_bit = i_n & target

            if x_bit:
                i_x = i_x << 1
                continue
            
            if n_bit:
                res = res | i_x
                
            i_n = i_n << 1
            i_x = i_x << 1
        
        return res

            
            
            



        
            
            
            

            

        