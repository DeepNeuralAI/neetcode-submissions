# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
   
        if head is None or (n == 1 and head.next is None):
            return None
        
        dummy = ListNode(0, head)
        left = right = dummy
        count = 0

        while count <= n and right:
            count += 1
            right = right.next
        
        while right:
            left = left.next
            right = right.next
        
        # if left.next÷:
        left.next = left.next.next
        

        return dummy.next


        

        

        

        

        