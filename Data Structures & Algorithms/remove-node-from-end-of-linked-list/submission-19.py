# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # Recursive Approach
        self.index = 0
        def remove(node):
            if node is None:
                return None
            
            next_node = remove(node.next)
            self.index += 1
            
            if self.index == n + 1:
                node.next = node.next.next
            
            return node
        
        dummy = ListNode(0, head) 
        remove(dummy)
        return dummy.next
        

            





        