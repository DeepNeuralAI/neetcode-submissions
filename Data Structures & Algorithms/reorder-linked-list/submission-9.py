# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Split linked list in halves
        # 2. Reverse second half
        # 3. Merge list 

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        prev = None
        curr = head2
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        head2 = prev
        dummy = ListNode()
        curr = dummy
        tmp1, tmp2 = head, head2

        while tmp1 and tmp2:
            curr.next = tmp1
            curr = curr.next
            tmp1 = tmp1.next

            curr.next = tmp2
            tmp2 = tmp2.next
            curr = curr.next
        
        if tmp1:
            curr.next = tmp1
        
        if tmp2:
            curr.next = tmp2
        
        head = dummy.next



        