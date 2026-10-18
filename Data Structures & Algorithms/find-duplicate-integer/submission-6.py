class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Invariant - idx is the node, value[idx] is next pointer
        # Cycle occurs - use hare and tortoise to find cycle
        # Then find start of cycle, and that will be repeated number

        fast = slow = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

        