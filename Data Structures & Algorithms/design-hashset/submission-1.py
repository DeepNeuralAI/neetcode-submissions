class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.data = [Node(-1)] * 10_000
        self.size = 0
        

    def add(self, key: int) -> None:
        idx = self.hash(key)
        curr = self.data[idx]

        while curr.next:
            curr = curr.next
            if curr.key == key:
                return
        
        curr.next = Node(key)
        self.size += 1


    def remove(self, key: int) -> None:
        idx = self.hash(key)
        curr = self.data[idx]

        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        
        self.size -= 1
        

    def contains(self, key: int) -> bool:
        idx = self.hash(key)
        curr = self.data[idx]

        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        
        return False
    
    
    def hash(self, key):
        return (key % 10_000)


        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)