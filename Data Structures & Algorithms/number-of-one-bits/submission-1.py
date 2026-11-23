class Solution:
    def hammingWeight(self, n: int) -> int:
        count = self.convertToBinary(n)
        return count


    def convertToBinary(self, n):
        if n == 0 or n == 1:
            return n
        res = []
        cnt = 0
        
        while n > 1:
            rem = n % 2
            n = n >> 1
            res.append(rem)

            if rem == 1:
                cnt += 1
        
        if n == 1:
            res.append(n)
            cnt += 1
        
        # res.reverse()
        return cnt


        