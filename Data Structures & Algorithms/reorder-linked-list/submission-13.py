# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Split in Half
        # Reverse second half 
        # Merge two halves back

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_head = slow.next
        slow.next = None

        new_head = self.reverse(second_head)
        dummy = ListNode(-1, None)
        curr = dummy

        while head and new_head:
            curr.next = head
            head = head.next

            curr = curr.next
            curr.next = new_head
            new_head = new_head.next
            curr = curr.next
        
        if new_head:
            curr.next = new_head
        
        if head:
            curr.next = head
        
        head = dummy.next
        



    

    def reverse(self, node):
        if not node or not node.next:
            return node
        

        head = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return head
    



        