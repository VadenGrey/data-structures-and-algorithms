from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        if self.rear:
            self.rear.next = value
            self.rear = self.rear.next
            return
        self.rear = self.front = value

    def dequeue(self, value):
        dequeued = self.front
        if dequeued.an:
            while dequeued.an != value:
                self.front = self.front.next
                dequeued = self.front
                if dequeued is None:
                    return None


        return dequeued.an


class Dog:
    def __init__(self, next=None):
        self.an = "dog"
        self.next = next


class Cat:
    def __init__(self, next=None):
        self.an = "cat"
        self.next = next
