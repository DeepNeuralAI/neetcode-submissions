class Node:
    def __init__(self, key, next = None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.data = [Node(-1) for _ in range(10_000)]

    def add(self, key: int) -> None:
        root = self.data[self.getIdx(key)]
        curr = root

        while curr and curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        
        curr.next = Node(key)

    def remove(self, key: int) -> None:
        root = self.data[self.getIdx(key)]
        curr = root

        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            
            curr = curr.next
        

    def contains(self, key: int) -> bool:
        root = self.data[self.getIdx(key)]
        curr = root

        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        
        return False
    
    def getIdx(self, key):
        return key % 10_000
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)