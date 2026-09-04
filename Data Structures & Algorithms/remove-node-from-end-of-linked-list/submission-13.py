# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
   
        if head is None or (n == 1 and head.next is None):
            return None
        
        # Recursive Solution
        def remove(node, n):
            if node is None:
                return 0
            
            index = remove(node.next, n) + 1

            if index == (n + 1):
                node.next = node.next.next
            
            return index
        
        index = remove(head, n)
        if n == index:
            return head.next
        return head
            

            



        

        

        

        

        