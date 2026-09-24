# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find the middle 
        # 2. Cut the linked list at the middle
        # 3. Reverse the second half
        # 4. Merge the two halves back

        # 1.
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second_half = slow.next
        slow.next = None

        curr = second_half
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        second = prev
        first = head
        temp = ListNode(0)
        curr = temp
        
        while first and second:
            curr.next = first
            first = first.next
            curr = curr.next
            
            curr.next = second
            second = second.next
            curr = curr.next
        
        if first:
            curr.next = first
        
     
        head = temp.next

        