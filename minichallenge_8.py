# Pilas y colas: Implementa las operaciones básicas de una pila y/o una cola para 5 elementos.
class Stack:
    def __init__(self, max_size=5):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)
            print(f"Pushed {item} to the stack")
        else:
            print("Stack is full. Cannot push more items.")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. Cannot peek.")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# Test the Stack
print("Testing Stack:")
stack = Stack()

for i in range(1, 7):  # Try to push 6 elements
    stack.push(i)

print("Stack:", stack)
print("Stack size:", stack.size())
print("Top element:", stack.peek())

for _ in range(6):  # Try to pop 6 elements
    popped = stack.pop()
    if popped:
        print(f"Popped: {popped}")

print("Is stack empty?", stack.is_empty())
print()
