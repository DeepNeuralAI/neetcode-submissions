# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        prevGroup = dummy

        while True:
            kthNode = prevGroup
            steps = 0

            while steps < k and kthNode:
                kthNode = kthNode.next
                steps += 1
            
            if not kthNode:
                break
            
            curr = prevGroup.next
            next_group = kthNode.next
            new_head = self.reverse(curr, next_group)

            prevGroup.next = new_head
            curr.next = next_group
            prevGroup = curr

        return dummy.next


    def reverse(self, start, end):
        prev = None
        curr = start
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev




