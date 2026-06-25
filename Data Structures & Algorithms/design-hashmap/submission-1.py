class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.map = [Node(-1, -1) for _ in range(1_000)]

    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        curr = self.map[idx]

        while curr and curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            
            curr = curr.next
        
        curr.next = Node(key, value)
        

    def get(self, key: int) -> int:
        idx = self.hash(key)
        head = self.map[idx]
        curr = head.next

        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        
        return -1
        

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        curr = self.map[idx]

        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        
    def hash(self, key):
        return key % 1_000


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)