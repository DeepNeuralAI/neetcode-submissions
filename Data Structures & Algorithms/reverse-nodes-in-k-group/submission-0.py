# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prevGroup = dummy

        while True:
            temp = prevGroup

            for _ in range(k):
                temp = temp.next

                if not temp:
                    return dummy.next
            
            kth = temp
            groupNext = kth.next
            kth.next = None
            groupStart = prevGroup.next
            groupHead = self.reverse(groupStart)
            
            prevGroup.next = groupHead
            groupStart.next = groupNext
            prevGroup = groupStart
        
        return dummy.next
    
    def reverse(self, head):
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node
        
        return prev