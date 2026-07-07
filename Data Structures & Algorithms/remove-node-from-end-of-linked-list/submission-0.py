# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        
        curr = fast = dummy

        for _ in range(n):
            fast = fast.next
        
        while fast and fast.next:
            curr = curr.next
            fast = fast.next
        
        nth_node = curr.next
        curr.next = nth_node.next

        return dummy.next