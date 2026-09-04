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
        original_to_new_node_map = {}
        curr = head

        while curr:
            original_to_new_node_map[curr] = Node(curr.val)
            curr = curr.next
        
        dummy = Node(0)
        temp = dummy
        curr = head
        
        while curr:
            new_node = original_to_new_node_map[curr]
            if curr.random:
                new_node.random = original_to_new_node_map[curr.random]
            
            if curr.next:
                new_node.next = original_to_new_node_map[curr.next]
            
            temp.next = new_node
            temp = temp.next
            curr = curr.next
        
        return dummy.next


        