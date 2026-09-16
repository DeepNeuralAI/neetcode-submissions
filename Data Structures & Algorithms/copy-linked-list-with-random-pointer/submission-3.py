"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original_to_copy = {}
        curr = head


        while curr:
            copy = Node(curr.val)
            original_to_copy[curr] = copy
            curr = curr.next
        
        curr = head
        dummy = Node(-1)
        temp = dummy

        while curr:
            copy = original_to_copy[curr]
            if curr.next:
                copy.next = original_to_copy[curr.next]
            
            if curr.random:
                copy.random = original_to_copy[curr.random]
            
            temp.next = copy
            temp = temp.next
            curr = curr.next
        
        return dummy.next