class Queue:
    def __init__(self):
        self.rear = -1
        self.data = []

    def enqueue(self, value):
        self.data.append(value)
        self.rear += 1

    def dequeue(self):
        value = self.data[0]
        del self.data[0]
        self.rear -= 1
        return value

    def print(self):
        print(self.rear)
        print(self.data)
