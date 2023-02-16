from data_structures.binary_tree import BinaryTree

def breadth_first(tree):
    vals = []
    queue = []
    if tree.root:
        queue.append(tree.root)
    else:
        return vals

    while len(queue) > 0:
        current = queue.pop(0)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        vals.append(current.value)

    return vals

