# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        
        node_before_sublist, current = dummy, head

        for i in range(left - 1):
            current = current.next
            node_before_sublist = node_before_sublist.next
        

        sublist_tail = current

        previous = None
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        
        node_before_sublist.next = previous
        sublist_tail.next = current

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

        