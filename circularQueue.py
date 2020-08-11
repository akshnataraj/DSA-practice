class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self._queue = [None] * k #the basic 
        self._capacity = k 
        self._len = 0 
        #The first three as one group and the last
        self._front = 0
        #self._rear is not necessary, because rear = front + length -1


    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull(): return False
        avail = (self._front + self._len) % (self._capacity)
        self._queue[avail] = value 
        self._len += 1
        return True 

       
    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False 
        self._queue[self._front] = None #overrode the current node 
        self._front = (self._front+1) % self._capacity 
        self._len -= 1
        return True

        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if not self.isEmpty():
            return self._queue[self._front]
        else:
            return -1
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if not self.isEmpty():
            _rear = (self._front + self._len - 1) % self._capacity
            return self._queue[_rear]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self._len == 0 
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self._len == self._capacity   


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()