from data_structures.stack import Stack

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class PseudoQueue:

    def __init__(self):
        r_stack = Stack()
        f_stack = Stack()
        self.front = f_stack.top
        self.rear = r_stack.top

    def enqueue(self, value):
        if self.rear:
            self.rear.next = Node(value)
            self.rear = self.rear.next
            return
        self.rear = self.front = Node(value)

    def dequeue(self):
        dequeued = self.front
        self.front = self.front.next
        return dequeued.value

