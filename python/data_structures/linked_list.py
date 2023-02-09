class LinkedList:
    """
    Class that creates a linked list
    """

    def __init__(self):
        self.head = None


    def __str__(self):
        current = self.head
        stringval = ""
        while current is not None:
            stringval += f"{{ {str(current.value)} }} -> "
            current = current.next
        stringval += "NULL"
        return stringval


    def insert(self, value):
        self.head = Node(value, self.head)


    def append(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)


    def insert_before(self, before, value):
        try:
            current = self.head
            if current.value == before:
                self.head = Node(value, current)
            else:
                while current.value != before:
                    previous = current
                    current = current.next
                previous.next = Node(value, current)
        except Exception as e:
            raise TargetError(e)


    def insert_after(self, after, value):
        try:
            current = self.head
            after_val = self.head.next
            if current.value == after:
                self.head.next = Node(value, after_val)
            else:
                while current.value != after:
                    current = current.next
                current.next = Node(value, after_val)
        except Exception as e:
            raise TargetError(e)


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


class TargetError(Exception):
    pass
