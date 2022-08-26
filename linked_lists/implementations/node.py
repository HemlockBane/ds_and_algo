class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None

    def __str__(self):
        if self is None:
            return "Empty Node"
        return f"{str(self.data)}"