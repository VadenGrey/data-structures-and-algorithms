class BinaryTree:
    """
    A DS that has Nodes that have a left and right value
    """

    def __init__(self):
        self.root = None

    def post_order(self, root=None, nodes=None):
        """
        traverse Left, Right, Root
        """
        if root is None:
            root = self.root

        if nodes is None:
            nodes = []

        if root.left:
            self.post_order(root.left, nodes)

        if root.right:
            self.post_order(root.right, nodes)

        nodes.append(root.value)

        return nodes

    def pre_order(self, root=None, nodes=None):
        """
        traverse Root, Left, Right
        """
        if root is None:
            root = self.root

        if nodes is None:
            nodes = []

        nodes.append(root.value)

        if root.left:
            self.pre_order(root.left, nodes)

        if root.right:
            self.pre_order(root.right, nodes)

        return nodes

    def in_order(self, root=None, nodes=None):
        """
        traverse Left, Root, Right
        """
        if root is None:
            root = self.root

        if nodes is None:
            nodes = []

        if root.left:
            self.in_order(root.left, nodes)

        nodes.append(root.value)

        if root.right:
            self.in_order(root.right, nodes)

        return nodes

    def find_maximum_value(self):
        root = self.root
        nodes = []

        if root.left:
            self.in_order(root.left, nodes)

        nodes.append(root.value)

        if root.right:
            self.in_order(root.right, nodes)

        nodes.sort()

        return nodes[-1]

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
