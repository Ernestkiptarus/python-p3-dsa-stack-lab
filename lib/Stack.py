class Stack:
    def __init__(self, limit=None):
        self.stack = []
        self.limit = limit

    def push(self, item):
        if self.is_full():
            raise Exception("Stack is full")
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)

    def empty(self):
        return len(self.stack) == 0

    def is_full(self):
        if self.limit is not None:
            return len(self.stack) >= self.limit
        else:
            return False

    def search(self, value):
        if value in self.stack:
            return len(self.stack) - self.stack.index(value) - 1
        else:
            return -1
