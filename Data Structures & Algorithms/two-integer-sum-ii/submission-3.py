class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n - 1
        res = []

        while i < j:
            candidate = numbers[i] + numbers[j]

            if candidate == target:
                return [i + 1, j + 1]
            
            if candidate < target:
                i += 1
            else:
                j -= 1
        
        return [-1, -1]

        