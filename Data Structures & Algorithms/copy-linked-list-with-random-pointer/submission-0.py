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
        originalToCopy = {}

        while curr:
            originalToCopy[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        dummy = Node(-1)

        newCurr = dummy
        while curr:
            new_node = originalToCopy[curr]

            if curr.random:
                new_node.random = originalToCopy[curr.random]
            
            newCurr.next = new_node
            newCurr = newCurr.next

            curr = curr.next

        return dummy.next