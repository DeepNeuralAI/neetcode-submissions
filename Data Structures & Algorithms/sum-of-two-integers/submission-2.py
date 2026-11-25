class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Restrict a to 32 bits only!
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF # 2^31 - 1
        
        while b != 0:
            total = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK
            
            a = total
            b = carry
        
        if a > MAX_INT:
            a = ~(a ^ MASK)
        
        return a



        
        

        