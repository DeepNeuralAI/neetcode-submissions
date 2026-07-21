class MyHashSet:

    def __init__(self):
        self.data = [Node(-1) for _ in range(10_000)]

        
    def add(self, key: int) -> None:
        idx = self.getIdx(key)
        head = self.data[idx]
        curr = head

        while curr.next:
            if curr.next.value == key:
                return
            curr = curr.next
        
        curr.next = Node(key)
        return
        
    def remove(self, key: int) -> None:
        idx = self.getIdx(key)
        head = self.data[idx]
        curr = head

        while curr.next:
            if curr.next.value == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        

    def contains(self, key: int) -> bool:
        idx = self.getIdx(key)
        head = self.data[idx]
        curr = head

        while curr.next:
            if curr.next.value == key:
                return True
            curr = curr.next
        
        return False
    

    def getIdx(self, key):
        return key % 10_000


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)