# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find Midpoint
        if head is None or head.next is None:
            return
        
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        first = head
        second = slow.next
        slow.next = None
        
        # Reverse
        second = self.reverseLL(second)

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second

            second.next = tmp1
            first, second = tmp1, tmp2

    def reverseLL(self, head):
        prev, curr = None, head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev

        
            
        