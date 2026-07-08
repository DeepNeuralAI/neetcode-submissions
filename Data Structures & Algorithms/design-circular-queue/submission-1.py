class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = Node(-1)
        self.tail = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        new_node = Node(value)
        if self.isEmpty():
            self.head.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        front = self.head.next
        self.head.next = front.next

        if self.size == 1:
            self.tail = self.head
        
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.head.next.value
        
    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.tail.value
    
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()