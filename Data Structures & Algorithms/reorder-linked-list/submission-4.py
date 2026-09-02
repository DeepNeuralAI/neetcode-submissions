# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        idx_to_node = {}
        curr = head
        i = 0

        while curr:
            idx_to_node[i] = curr
            i += 1
            curr = curr.next
        
        n = len(idx_to_node)
        dummy = ListNode(-1)
        curr = dummy
        
        l = 0
        r = n - 1
        

        while l <= r:
            
            curr.next = idx_to_node[l]
            curr = curr.next
            
            if l == r:
                break
                
            curr.next = idx_to_node[r]
            curr = curr.next
            
            l += 1
            r -= 1
        
        curr.next = None

            


        