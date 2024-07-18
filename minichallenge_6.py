# Árbol binario de búsqueda (BST): Implementa solo la inserción en un árbol binario de búsqueda para 5 elementos.
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def inorder_traversal(self):
        def _inorder(node):
            if node:
                yield from _inorder(node.left)
                yield node.value
                yield from _inorder(node.right)

        return list(_inorder(self.root))


# Create a BST and insert 5 elements
bst = BinarySearchTree()
elements = [5, 3, 7, 2, 4]

for element in elements:
    bst.insert(element)

# Print the tree in order to verify correct insertion
print("BST elements in order:", bst.inorder_traversal())
