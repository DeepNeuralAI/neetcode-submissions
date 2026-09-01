# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 1:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head

        prevGroup = dummy

        while True:
            kth = prevGroup
            steps = 0

            while steps < k and kth:
                kth = kth.next
                steps += 1
            
            if not kth:
                break
            
            groupNext = kth.next
            curr = prevGroup.next
            prev = groupNext

            while curr != groupNext:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            
            temp = prevGroup.next
            temp.next = groupNext
            prevGroup.next = kth
            prevGroup = temp


        return dummy.next
            

        


        

       

            



