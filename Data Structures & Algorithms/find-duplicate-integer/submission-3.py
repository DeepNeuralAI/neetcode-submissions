class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd Cycle Detection?
        slow = fast = 0

        # Stop when cycle detected
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


        