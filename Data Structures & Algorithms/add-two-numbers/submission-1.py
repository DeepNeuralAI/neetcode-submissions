# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        carry_over = 0

        while l1 and l2:
            new_sum = l1.val + l2.val + carry_over

            carry_over = new_sum // 10
            temp.next = ListNode(new_sum % 10)
            
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            new_sum = l1.val + carry_over
            temp.next = List
            carry_over = new_sum // 10
            temp.next = ListNode(new_sum % 10)
            
            temp = temp.next
            l1 = l1.next
        
        while l2:
            new_sum = l2.val + carry_over
            carry_over = new_sum // 10
            temp.next = ListNode(new_sum % 10)
            temp = temp.next
            l2 = l2.next
        
        if carry_over:
            temp.next = ListNode(carry_over)
        
        return dummy.next
