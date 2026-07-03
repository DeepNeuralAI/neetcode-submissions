class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class MyHashSet:

    def __init__(self):
        self.data = [Node(-1) for _ in range(10_000)]
        self.size = 0
        
    def add(self, key: int) -> None:
        idx = self.hash(key)
        head = self.data[idx]
        curr = head
        
        while curr and curr.next:
            if curr.next.data == key:
                return
            curr = curr.next
        
        curr.next = Node(key)
        
    def remove(self, key: int) -> None:
        idx = self.hash(key)
        head = self.data[idx]
        curr = head

        while curr and curr.next:
            if curr.next.data == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        

    def contains(self, key: int) -> bool:
        idx = self.hash(key)
        head = self.data[idx]
        curr = head
        
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        
        return False

    def hash(self, key):
        return key % 10_000


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)