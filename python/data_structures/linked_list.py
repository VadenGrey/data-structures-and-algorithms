class LinkedList:
    """
    Class that creates a linked list
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        string_values = ""
        while current is not None:
            string_values += f"{{ {str(current.value)} }} -> "
            current = current.next
        string_values += "NULL"
        return string_values

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError:
    pass
