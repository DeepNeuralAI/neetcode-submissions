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


    def interleave(self, h1, h2):
        dummy = ListNode(-1)
        curr = dummy
        
        while h1 and h2:
            curr.next = h1
            h1 = h1.next
            curr = curr.next

            curr.next = h2
            h2 = h2.next
            curr = curr.next    

        if h1:
            curr.next = h1
        
        if h2:
            curr.next = h2

        
        
        