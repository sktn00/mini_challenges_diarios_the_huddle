# Piloto de eventos (Priority Queue): Implementa una cola de prioridad utilizando una lista para insertar y eliminar 5 elementos.
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def delete_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_val

    def _heapify_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent)

    def _heapify_down(self, i):
        max_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left

        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right

        if i != max_index:
            self.swap(i, max_index)
            self._heapify_down(max_index)

    def __str__(self):
        return str(self.heap)


# Test the PriorityQueue
pq = PriorityQueue()

# Insert elements
pq.insert(5)
pq.insert(2)
pq.insert(7)
pq.insert(1)
pq.insert(3)

print("Priority Queue after insertions:", pq)

# Delete max elements
print("Deleted max:", pq.delete_max())
print("Deleted max:", pq.delete_max())
print("Deleted max:", pq.delete_max())

print("Priority Queue after deletions:", pq)
