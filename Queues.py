class CircularQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * CircularQueue.DEFAULT_CAPACITY
        self._size= 0
        self._front= 0

    def __len__(self):
        return self._size

    def is_Empty(self):
        return self._size

    def first(self):
        if self.is_Empty():
            raise Exception("The Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        if self.is_Empty():
            raise Exception("The Queue is empty for dequeue operation")
        front = [self._front + 1] % len(self._data)
        dequeued_element = self.data[self._front]
        self._data[self._front]= None #garbage collection


    def enqueue(self,element):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        tail= (self._front+ self._size)% len(self._data)
        self._data[tail]= element
        self._size =self._size + 1


    def _resize(self, new_capacity):
        pass
    class Empty(Exception):
        pass
if __name__ =="__main__":
        object_queue = CircularQueue()
        insert_elements= [11,22,33,44,55]
        for element in (insert_elements):
            object_queue.enqueue(element)
            print(f"Added Element:{element}")
            print(f"The new size of the queues:{object_queue._size}")

            print("\nCurrent Queue Representation:")






