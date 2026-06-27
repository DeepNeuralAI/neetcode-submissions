class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Using sorted invariant
        i = 0
        j = len(numbers) - 1

        while i < j:
            candidate = numbers[i] + numbers[j]

            if candidate == target:
                return [i + 1, j + 1]
            elif candidate < target:
                i += 1
            else:
                j -= 1
        return []
