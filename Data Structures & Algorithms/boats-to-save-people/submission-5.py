class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        # [1, 2, 2, 3, 3], limit = 3
        # 
        # boats: 4
        l = 0
        r = len(people) - 1

        while l <= r:
            remaining = limit - people[r]

            if remaining < people[l]:
                r -= 1
            else:
                l += 1
                r -= 1
            
            boats += 1
        
        return boats