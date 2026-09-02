# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        l = 0
        r = n - 1

        return self.mergeK(lists, l, r)

    def mergeK(self, lists, l, r):
        if l == r:
            return lists[l]
        
        if l > r:
            return
        
        m = (l + r) // 2
        h1 = self.mergeK(lists, l, m)
        h2 = self.mergeK(lists, m + 1, r)
        return self.merge(h1, h2)
        


    def merge(self, l1, l2):
        dummy = ListNode(-1)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        if l1:
            curr.next = l1
        
        if l2:
            curr.next = l2
        
        return dummy.next