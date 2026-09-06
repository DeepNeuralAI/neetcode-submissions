# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Iterative Approach
        if head is None or head.next is None:
            return None
        
        # def remove(node):
        #     if node.next is None:
        #         return 0
            
        #     index = 1 + remove(node.next)
        #     if index == n:
        #         node_removed = node.next
        #         node.next = node_removed.next
        #     return index

        
        dummy = ListNode(0, head)
        curr = dummy

        # Place right pointer n places away
        left = dummy
        right = head
        steps = 0
        
        while steps < n and right:
            right = right.next
            steps += 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        
        return dummy.next
