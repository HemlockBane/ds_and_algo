from collections import deque


class QueueWithDeque:
    def __init__(self):
        self.storage = deque()

    def is_empty(self):
        return len(self.storage) == 0

    def enqueue(self, data):
        self.storage.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.storage.popleft()

    def peek(self):
        if self.is_empty():
            return None
        return self.storage[0]

    def length(self):
        return len(self.storage)


class QueueWithList:
    def __init__(self):
        self.storage = []

    def is_empty(self):
        return len(self.storage) == 0

    def enqueue(self, data):
        self.storage.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.storage.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.storage[0]

    def length(self):
        return len(self.storage)
