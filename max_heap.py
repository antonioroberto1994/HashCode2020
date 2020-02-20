from TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue

# To obtain a MaxHeap simply invert the sign of the key.
# So when we insert an element, we give it a negative key. In this way the module of
# the first element is the biggest.
# We define the methods max and remove_max, they recall respectively min and remove_min,
# they also return the key with the inverted sign.


class MaxHeap(HeapPriorityQueue):

    def __init__(self, contents=()):
        self._data = [self._Item(-k,v) for k,v in contents] #empty by default
        if len(self._data) > 1: 
            self._heapify() 

    def _heapify(self): 
        start = self._parent(len(self) -1) #start at parent of last leaf
        for j in range(start, -1, -1):  #going to and including the root
            self._downheap(j)

    def add(self, key, value):
        """Appends item to the heap. The key has changed its sign."""
        self._data.append(self._Item(-key, value))
        self._upheap(len(self._data) - 1)

    def max(self):
        """Return but do not remove (k,v) tuple with maximum key."""
        key, value = self.min()
        return -key, value

    def remove_max(self):
        """Remove and return (k,v) tuple with maximum key."""
        key, value = self.remove_min()
        self._downheap(0)
        return -key, value

