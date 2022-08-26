from linked_lists.implementations import Node


class LinkedListWithTail:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = self.head

    def is_empty(self):
        return self.head is None

    def insert_at_start(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

        if self.tail is None:
            self.tail = self.head

    def insert_at_end(self, data):
        if self.is_empty():
            self.insert_at_start(data)
            return

        node = Node(data)
        self.tail.next = node
        self.tail = node

    def insert_after(self, node: Node, data):
        # If the idx is equal to the length (i.e. if the list is empty or if it is last node)
        # Else,
        # - get the prev node
        # - store next in temp
        # - connect prev to the new node
        # - connect the new node to temp
        if self.tail == node:
            self.insert_at_end(data)
            return

        new_node = Node(data)

        temp = node.next
        node.next = new_node
        new_node.next = temp

    def get_node_at(self, idx: int):
        counter = 0
        current_node = self.head

        while current_node is not None and counter < idx:
            current_node = current_node.next
            counter = counter + 1

        return current_node

    def remove_first(self):
        if self.is_empty():
            return None

        data = self.head.data
        self.head = self.head.next
        if self.is_empty():
            self.tail = None
        return data

    def remove_last(self):
        # If head is the last node is null, pop()

        # Loop to the node before the last node
        # Get its value
        # Point tail to the node before tail
        # Set next node to null
        # Return the data

        # None
        # [1] - None
        # [1] - [2] - None
        # [1] - [2] - [3] -

        if self.is_empty() or self.head.next is None:
            return self.remove_first()

        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next

        data = self.tail.data
        self.tail = current_node
        self.tail.next = None
        return data

    def remove_after(self, node: Node):
        # If node is null or node.next is null, return nill
        # If node.next is tail
        # - set tail to current node
        # - set node.next to null
        # If node is non-tail
        # - set node.next to node.next.next

        if node is None or node.next is None:
            return None

        data = node.next.data
        if node.next == self.tail:
            self.tail = node
            node.next = None
            return data

        node.next = node.next.next
        return data

    def print_all(self):
        if self.is_empty():
            print("Empty List")

        temp = self.head
        while temp:
            is_not_tail = temp != self.tail
            end = f"{'->' if is_not_tail else chr(10)}"
            print(str(temp), end=end)
            temp = temp.next
