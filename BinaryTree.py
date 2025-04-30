class Node:
    def __init__(self, key):
        self.left = None  # Left child
        self.right = None  # Right child
        self.value = key  # Node value

class BinaryTree:
    def __init__(self):
        self.root = None  # Root of the binary tree

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursively(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursively(node.right, key)

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        if node is None or node.value == key:
            return node
        if key < node.value:
            return self._search_recursively(node.left, key)
        return self._search_recursively(node.right, key)

    def inorder_traversal(self):
        return self._inorder_recursively(self.root)

    def _inorder_recursively(self, node):
        return (self._inorder_recursively(node.left) if node.left else []) + \
               [node.value] + \
               (self._inorder_recursively(node.right) if node.right else [])

    def preorder_traversal(self):
        return self._preorder_recursively(self.root)

    def _preorder_recursively(self, node):
        return [node.value] + \
               (self._preorder_recursively(node.left) if node.left else []) + \
               (self._preorder_recursively(node.right) if node.right else [])

    def postorder_traversal(self):
        return self._postorder_recursively(self.root)

    def _postorder_recursively(self, node):
        return (self._postorder_recursively(node.left) if node.left else []) + \
               (self._postorder_recursively(node.right) if node.right else []) + \
               [node.value]

# Example usage
if __name__ == "__main__":
    tree = BinaryTree()
    values = [7, 3, 9, 1, 5, 8, 10]
    
    for value in values:
        tree.insert(value)

    print("In-order traversal:", tree.inorder_traversal())
    print("Pre-order traversal:", tree.preorder_traversal())
    print("Post-order traversal:", tree.postorder_traversal())

    search_value = 5
    found_node = tree.search(search_value)
    if found_node:
        print(f"Value {search_value} found in the tree.")
    else:
        print(f"Value {search_value} not found in the tree.")
