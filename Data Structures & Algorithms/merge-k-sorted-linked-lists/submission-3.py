# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        min_heap = []
        dummy = ListNode(-1)
        curr = dummy

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i, head))
        
        while min_heap:
            value, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = node

            if node.next:
                node = node.next
                heapq.heappush(min_heap, (node.val, i, node))


        return dummy.next
        
        