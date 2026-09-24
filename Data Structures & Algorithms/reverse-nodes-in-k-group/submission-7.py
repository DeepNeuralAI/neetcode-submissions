# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy
        curr = head

        while curr:
            kth = prevGroup
            steps = 0
            while steps < k and kth:
                kth = kth.next
                steps += 1
            
            if not kth:
                break
            
            next_group_head = kth.next
            kth.next = None

            # Reverse
            prev = None
            temp = curr
            while temp:
                next_node = temp.next
                temp.next = prev
                prev = temp
                temp = next_node
            
            curr.next = next_group_head
            prevGroup.next = prev
            prevGroup = curr
            curr = next_group_head
        

        return dummy.next
            
            


        