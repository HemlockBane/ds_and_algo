class Stack:
    def __init__(self):
        self.storage = []

    def push(self, data):
        self.storage.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.storage.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.storage[-1]

    def is_empty(self):
        return len(self.storage) == 0

    def length(self):
        return len(self.storage)