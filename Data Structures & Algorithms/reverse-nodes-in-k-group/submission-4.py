# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy
        
        while True:
            kth = prevGroup
            steps = 0
            
            while steps < k and kth:
                kth = kth.next
                steps += 1
            
            if not kth:
                break
            
            next_group = kth.next
            kth.next = None
            
            curr = prevGroup.next
            new_group_head = self.reverse(start = curr, end = next_group)
            
            prevGroup.next = new_group_head
            curr.next = next_group
            prevGroup = curr

        return dummy.next
    

    def reverse(self, start, end):
        curr = start
        prev = None

        while curr and curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
            
            

        