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

        if head is None:
            return head

        while curr:
            next_node = curr.next
            random_node = curr.random

            if curr not in original_to_copy:
                original_to_copy[curr] = Node(curr.val)
            
            if next_node not in original_to_copy:
                original_to_copy[next_node] = Node(next_node.val) if next_node else None
               
            
            if random_node not in original_to_copy:
                original_to_copy[random_node] = Node(random_node.val) if random_node else None
            
            original_to_copy[curr].next = original_to_copy[next_node]
            original_to_copy[curr].random =  original_to_copy[random_node]
            
            curr = curr.next
        
        return original_to_copy[head]

            


        