# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prevGroup = dummy

        while prevGroup:
            kth = self.getKth(prevGroup, k)

            if not kth:
                break
            
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
    
    def getKth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        
        return node