# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        
        prev, curr = dummy, head

        for i in range(left - 1):
            curr = curr.next
            prev = prev.next
        

        sublist_tail = curr

        pre = None
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = pre
            pre = curr
            curr = next_node
        
        next_node = curr
        sublist_head = pre

        prev.next = sublist_head
        sublist_tail.next = next_node

        return dummy.next



    

    def reverseList(self, head):
        if not head:
            return None
        
        curr = head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev

        