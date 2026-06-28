class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        l = 0
        r = n - 1
        numBoats = 0

        people.sort()

        while l <= r:
            if people[l] + people[r] <= limit:
                numBoats += 1
                l += 1
                r -= 1
            else:
                numBoats += 1
                r -= 1
        return numBoats
        