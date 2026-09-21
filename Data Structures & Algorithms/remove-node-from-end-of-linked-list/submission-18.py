# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Recursive Approach
        self.index = n
        def remove(node):
            if node is None:
                return None
            
            node.next = remove(node.next)
            self.index -= 1
            
            if self.index == 0:
                return node.next
            
            return node
        
        return remove(head)
        

            





        