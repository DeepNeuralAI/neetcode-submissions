class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        n = len(people)

        l = 0
        r = n - 1

        while l <= r:
            total_weight = people[l] + people[r]

            if total_weight > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            boats += 1
        
        return boats

        