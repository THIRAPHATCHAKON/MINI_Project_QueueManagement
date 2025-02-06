class StackLIFO:
    def __init__(self, max_size):
        self.stack = []
        self.top = -1
        self.max_size = max_size
        
    def push(self, element):
        if self.isFull():
            raise Exception("Stack is full")
        self.top += 1
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        element = self.stack[self.top]
        self.top -= 1
        return element

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.stack[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top + 1 == self.max_size

    def size(self):
        return self.top + 1


if __name__ == "__main__":
    max_size = 5
    slifo = StackLIFO(max_size)

    slifo.push(6)
    slifo.push(9)
    slifo.push(13)
    slifo.push(18)

    if slifo.isFull():
        print("Stack is full")

    if slifo.isEmpty():
        print("Stack is empty")

    for _ in range(10):
        try:
            value = slifo.pop()
            print(f"Pop = {value}")
        except Exception as e:
            print(e)
            break