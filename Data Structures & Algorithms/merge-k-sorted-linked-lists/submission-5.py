# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        curr = dummy

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        while heap:
            value, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, i, node))
        
        return dummy.next

        



        