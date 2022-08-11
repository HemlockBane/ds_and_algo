from stacks.implementation.stack_with_list import Stack


class QueueWithStacks:
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, data):
        self.enqueue_stack.push(data)

    def dequeue(self):
        if self.dequeue_stack.is_empty():
            while not self.enqueue_stack.is_empty():
                data = self.enqueue_stack.pop()
                self.dequeue_stack.push(data)

        return self.dequeue_stack.pop()

    def peek(self):
        if self.dequeue_stack.is_empty():
            while not self.enqueue_stack.is_empty():
                data = self.enqueue_stack.pop()
                self.dequeue_stack.push(data)

        return self.dequeue_stack.peek()

    def is_empty(self):
        return self.enqueue_stack.is_empty() and self.dequeue_stack.is_empty()

    def length(self):
        return self.enqueue_stack.length() + self.dequeue_stack.length()

