from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    A BST is where values are stored in a way that makes finding and adding values very fast, structured so that values to the left are lesser than its parent node and values on the right are greater
    """

    def __init__(self):
        self.root = None
        pass

    def add(self, num):
        if not self.root:
            self.root = Node(num)
        else:
            current = self.root
            while current:
                if num > current.value:
                    if current.right is None:
                        current.right = Node(num)
                        return
                    current = current.right

                elif num < current.value:
                    if current.left is None:
                        current.left = Node(num)
                        return
                    current = current.left

    def contains(self, num):
        if not self.root:
            return False
        else:
            current = self.root
            while current:
                if num > current.value:
                    if current.right is None:
                        return current.value == num
                    current = current.right

                elif num < current.value:
                    if current.left is None:
                        return current.value == num
                    current = current.left

                else:
                    return True
