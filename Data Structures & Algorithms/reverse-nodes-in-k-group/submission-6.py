
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
            
            next_group = kth.next
            curr_head = curr
            
            prev = None
            while curr and curr != next_group:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            curr_head.next = next_group
            prevGroup.next = kth
            prevGroup = curr_head
            # curr = next_group
        
        return dummy.next