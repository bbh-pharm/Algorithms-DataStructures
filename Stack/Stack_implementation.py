class Stack:
    def __init__(self):
        self.arr = []

    def push(self, data):
        self.arr.append(str(data))

    def pop(self):
        object = None
        if self.isEmpty():
            print("Stack is empty")
        else:
            object = self.arr.pop(-1)

        return object

    def peek(self):
        object = None
        if self.isEmpty():
            print("Stack is empty")
        else:
            object = self.arr[-1]

        return object

    def isEmpty(self):
        empty = False
        if len(self.arr) == 0:
            empty = True

        return empty
