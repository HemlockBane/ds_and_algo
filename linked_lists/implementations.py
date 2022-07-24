class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data=data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_start(data)
            return

        new_node = Node(data)
        curr_node = self.head

        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def insert_after(self, node: Node, data):
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    def remove_at_start(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def remove_at_end(self):
        if self.head is None or self.head.next is None:
            self.remove_at_start()

        curr_node = self.head
        while curr_node.next.next is not None:
            curr_node = curr_node.next
        data = curr_node.next.data
        curr_node.next = None
        return data

    def get_node_at(self, index: int):
        counter = 0
        curr_node = self.head

        while curr_node.next is not None and counter < index:
            curr_node = curr_node.next
            counter = counter

        return curr_node

    def remove_after(self, node: Node):
        if node is None or node.next is None:
            return None

        data = node.next.data
        if node.next.next is None:
            node.next = None
            return data

        node.next = node.next.next
        return data
