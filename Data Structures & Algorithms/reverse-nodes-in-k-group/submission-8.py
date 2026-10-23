# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prevGroup = dummy
        curr = head
        while curr:
            steps = 0
            kth = prevGroup
            while kth and steps < k:
                steps += 1
                kth = kth.next
            
            if not kth:
                break
            
            nextGroup = kth.next
            kth.next = None

            prev = None
            tmp = curr
            while tmp:
                nextNode = tmp.next
                tmp.next = prev
                prev = tmp
                tmp = nextNode
            
            prevGroup.next = prev
            curr.next = nextGroup
            prevGroup = curr
            curr = nextGroup
        
        return dummy.next


        