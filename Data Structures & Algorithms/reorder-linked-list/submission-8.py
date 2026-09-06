# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle of list
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second_half_head = slow.next
        slow.next = None

        # Reverse the second half
        prev = None
        curr = second_half_head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        second_half_head = prev

        # Merge the two
        dummy = ListNode(0, head)
        curr = dummy
        temp1 = head
        temp2 = second_half_head
        
        
        while temp1 and temp2:
            curr.next = temp1
            temp1 = temp1.next
            curr = curr.next

            curr.next = temp2
            temp2 = temp2.next
            curr = curr.next
        
        if temp1:
            curr.next = temp1
        
        if temp2:
            curr.next = temp2
        
        head = dummy.next




        