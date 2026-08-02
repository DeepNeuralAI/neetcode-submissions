# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head)
    

    def reverse(self, node):
        if node is None or node.next is None:
            return node
        
        next_node = node.next
        new_head = self.reverse(next_node)
        next_node.next = node
        node.next = None
                
        return new_head

        