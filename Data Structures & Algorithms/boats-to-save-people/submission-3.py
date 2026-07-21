class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0

        l = 0
        r = len(people) - 1

        while l <= r:
            remain = limit - people[r]

            if l < r and remain >= people[l]:
                l += 1
            
            r -= 1
            boats += 1
        
        return boats

        