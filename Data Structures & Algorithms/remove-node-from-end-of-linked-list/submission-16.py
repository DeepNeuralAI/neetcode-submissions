# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        end = dummy
        start = dummy

        steps = 0
        while steps < (n + 1) and end:
            end = end.next
            steps += 1

        while end:
            start = start.next
            end = end.next
        
        start.next = start.next.next
        return dummy.next
        

            





        