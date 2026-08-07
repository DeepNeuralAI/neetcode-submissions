class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []

        cols = set()
        pos_diagonals = set()
        neg_diagonals = set()


        def backtrack(i):
            if i == n:
                return 1
            
            count = 0
            for c in range(n):
                if (c in cols or 
                    (i + c) in pos_diagonals or
                    (i - c) in neg_diagonals):
                    continue
                
                cols.add(c)
                pos_diagonals.add(i + c)
                neg_diagonals.add(i - c)

                count += backtrack(i + 1)

                cols.remove(c)
                pos_diagonals.remove(i + c)
                neg_diagonals.remove(i - c)
            
            return count

        return backtrack(0)


        