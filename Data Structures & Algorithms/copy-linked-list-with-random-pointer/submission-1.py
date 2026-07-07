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
        curr = head
        originalToCopy = {None: None}

        while curr:
            originalToCopy[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        dummy = Node(-1)

        newCurr = dummy
        
        while curr:
            copy = originalToCopy[curr]
            copy.random = originalToCopy[curr.random]
            copy.next = originalToCopy[curr.next]
            
            curr = curr.next

        return originalToCopy[head]