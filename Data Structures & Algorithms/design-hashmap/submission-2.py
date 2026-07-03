class Node:
    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.data = [Node(-1, -1) for _ in range(10_000)]
        
    def put(self, key: int, value: int) -> None:
        idx = self.getIdx(key)
        head = self.data[idx]
        curr = head

        while curr and curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            
            curr = curr.next
        
        curr.next = Node(key, value)
        
    def get(self, key: int) -> int:
        idx = self.getIdx(key)
        head = self.data[idx]
        curr = head

        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        
        return -1
        

    def remove(self, key: int) -> None:
        idx = self.getIdx(key)
        head = self.data[idx]
        curr = head

        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            
            curr = curr.next
        
    
    def getIdx(self, key):
        return key % 10_000
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)