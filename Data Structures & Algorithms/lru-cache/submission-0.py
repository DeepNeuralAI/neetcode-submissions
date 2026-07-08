class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.previous = self.head
        
        self.key_to_node = {}

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self.remove(node)
        self.addToFront(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self.get(key)
            return
        
        if self.isFull():
            # Remove the LRU node
            lru_node = self.tail.previous
            self.remove(lru_node)
            del self.key_to_node[lru_node.key]
        
        new_node = Node(key, value)
        self.key_to_node[key] = new_node
        self.addToFront(new_node)
        
    def addToFront(self, node):
        next_node = self.head.next
        self.head.next = node

        node.next = next_node
        node.previous = self.head
        next_node.previous = node
        self.size += 1

    
    def remove(self, node):
        previous = node.previous
        next_node = node.next

        previous.next = next_node
        next_node.previous = previous
        self.size -= 1
    
    def isFull(self):
        return self.size == self.capacity

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None
