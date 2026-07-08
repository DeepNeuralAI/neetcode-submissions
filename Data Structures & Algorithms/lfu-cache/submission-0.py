class LFUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.freq_to_nodes = {}
        self.key_to_node = {}
        self.minFreq = 0
        
    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self.updateFreq(node)
        return node.value

    def updateFreq(self, node):
        # Increases the frequency of the node and frequency mapping
        current_freq = node.count

        # Remove from current DLL
        cache = self.freq_to_nodes[node.count]
        cache.remove(node)

        if cache.isEmpty() and current_freq == self.minFreq:
            self.minFreq += 1

        new_freq = current_freq + 1

        if new_freq not in self.freq_to_nodes:
            self.freq_to_nodes[new_freq] = DLL()
        
        node.count = new_freq
        self.freq_to_nodes[new_freq].addToFront(node)

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self.updateFreq(node)
        else:
            if self.isFull():
                cache = self.freq_to_nodes[self.minFreq]
                lru_node = cache.tail.previous
                cache.remove(lru_node)
                del self.key_to_node[lru_node.key]
                self.size -= 1
                
            self.minFreq = 1
            new_node = Node(key, value)

            if self.minFreq not in self.freq_to_nodes:
                self.freq_to_nodes[self.minFreq] = DLL()
            
            self.freq_to_nodes[self.minFreq].addToFront(new_node)
            self.key_to_node[key] = new_node
            self.size += 1

    def isFull(self):
        return self.size == self.capacity


class DLL:
    def __init__(self):
        self.size = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.previous = self.head

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
    
    def isEmpty(self):
        return self.size == 0

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.previous = None
        self.count = 1
    
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)