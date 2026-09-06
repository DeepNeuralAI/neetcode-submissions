# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        def remove(node):
            if node.next is None:
                return 0
            
            index = 1 + remove(node.next)
            if index == n:
                node_removed = node.next
                node.next = node_removed.next
            return index
        
        dummy = ListNode(0, head)
        curr = dummy
        remove(curr)
        return dummy.next
