# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or head.next is None:
            return None
        
        # Find Mid point
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None

        # Reverse
        second = self.reverse(second)

        # Interleave
        self.interleave(head, second)


    def reverse(self, head):
        curr = head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev


    def interleave(self, head1, head2):
        h1, h2 = head1, head2
        while h2:
            h1_next = h1.next
            h2_next = h2.next

            h1.next = h2
            h2.next = h1_next

            h1 = h1_next
            h2 = h2_next

        
        
        