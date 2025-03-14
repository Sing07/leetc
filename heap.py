class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index-1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value

    def _sink_down(self,index):
        left_child = self._left_child(index)
        right_child = self._right_child(index)

        if left_child > right_child:
            self._swap(index, self.heap[left_child])
        
heap = MaxHeap()
heap.insert(99)
heap.insert(72)
heap.insert(61)
heap.insert(58)

print(heap.heap)

heap.insert(100)

print(heap.heap)

heap.insert(75)
print(heap.heap)


print(sorted([3, 2, 3, 1, 2, 4, 5, 5, 6]))