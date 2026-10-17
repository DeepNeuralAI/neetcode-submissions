# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two pointers - fast and slow
        # Move fast n - 1 steps ahead from dummy node

        dummy = ListNode(-1, head)
        steps = 0
        fast = slow = dummy

        while fast and steps < n + 1:
            fast = fast.next
            steps += 1
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next
        
        