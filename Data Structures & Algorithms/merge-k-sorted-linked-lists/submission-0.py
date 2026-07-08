# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        l = 0
        r = len(lists) - 1

        return self.mergeHelper(lists, l, r)
    
    def mergeHelper(self, lists, l, r):
        if l == r:
            return lists[l]
        
        if r - l == 1:
            return self.merge(lists[l], lists[r])
        
        mid = (l + r) // 2
        left = self.mergeHelper(lists, l, mid)
        right = self.mergeHelper(lists, mid + 1, r)

        return self.merge(left, right)
        



    def merge(self, head1, head2):
        dummy = ListNode(-1)
        curr1, curr2 = head1, head2
        curr = dummy

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            
            curr = curr.next
        
        if curr1:
            curr.next = curr1
        
        if curr2:
            curr.next = curr2
        
        return dummy.next