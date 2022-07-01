class Queue:

    def __init__(self):
        self.elements = []
        self.size = 0

    def dequeue(self):
        self.elements.pop(0)
        self.size -= 1

    def size(): return self.size

    def enqueue(self,data):
        self.elements.append(data)
        self.size += 1

    def front(self):
        return self.elements[0]

    def rear(self):
        return self.elements[len(self.elements)-1]

class Stack:

    def __init__(self):
        self.elements = []
        self.size = 0

    def size(): return self.size

    def pop(self):
        self.elements.pop(-1)
        self.size -= 1

    def push(self,data):
        self.elements.append(data)
        self.size += 1

    def front(self):
        return self.elements[0]

    def top(self):
        return self.elements[-1]