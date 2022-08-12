# You can also use the other queue implementation: QueueWithList
from queues.implementation.queue_with_deque import QueueWithDeque


class StackWithQueue:
    def __init__(self):
        self.queue_1 = QueueWithDeque()
        self.queue_2 = QueueWithDeque()

    def push(self, data):
        self.queue_1.enqueue(data)

    def pop(self):
        while self.queue_1.length() > 1:
            data = self.queue_1.dequeue()
            self.queue_2.enqueue(data)

        data = self.queue_1.dequeue()
        temp = self.queue_1
        self.queue_1 = self.queue_2
        self.queue_2 = temp

        return data

    def peek(self):
        while self.queue_1.length() > 1:
            data = self.queue_1.dequeue()
            self.queue_2.enqueue(data)

        data = self.queue_1.peek()
        temp = self.queue_1
        self.queue_1 = self.queue_2
        self.queue_2 = temp

        return data

    def is_empty(self):
        return self.queue_1.length() == 0