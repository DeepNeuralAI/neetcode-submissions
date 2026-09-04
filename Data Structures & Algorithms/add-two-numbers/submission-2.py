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

        while l1 or l2 or carry_over:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            new_sum = v1 + v2 + carry_over

            carry_over = new_sum // 10
            val = new_sum % 10
            temp.next = ListNode(val)
            
            
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
       
        # if carry_over:
        #     temp.next = ListNode(carry_over)
        
        return dummy.next
