from python_collections.priority_queue.heap_priority_queue import HeapPriorityQueue

class MaxHeap(HeapPriorityQueue):

    def __init__(self, contents=()):
        self._data = [self._Item(-k,v) for k,v in contents]
        if len(self._data) > 1: 
            self._heapify() 

    def _heapify(self): 
        start = self._parent(len(self) -1) 
        for j in range(start, -1, -1):  
            self._downheap(j)

    def add(self, key, value):
        self._data.append(self._Item(-key, value))
        self._upheap(len(self._data) - 1)

    def max(self):
        key, value = self.min()
        return -key, value

    def remove_max(self):
        key, value = self.remove_min()
        self._downheap(0)
        return -key, value

