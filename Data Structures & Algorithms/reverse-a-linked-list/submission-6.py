# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        def reverse(node):
            if node.next is None:
                return node
            
            next_node = node.next
            new_head = reverse(next_node)
            next_node.next = node
            node.next = None
            return new_head
        
        return reverse(head)
            

        