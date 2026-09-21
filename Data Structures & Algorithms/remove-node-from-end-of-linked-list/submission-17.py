# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Recursive Approach

        def remove(node):
            if node is None:
                return 0
            
            index = 1 + remove(node.next)
            if index == (n + 1):
                node.next = node.next.next
            
            return index
        
        dummy = ListNode(0, head)
        remove(dummy)
        return dummy.next
        

            





        