class Stack:

    top = -1

    def __init__(self):
        self.top = -1
        # this stack is implemented with Python list (array)
        self.data = []

    def size(self):
        return len(self.data)

    def push(self, value):
        # increment the size of data using append()
        self.data.append(value)
        self.top += 1

    def pop(self):
        self.top -= 1
        return self.data.pop()

    def isEmpty(self):
        size = self.size()
        if size == 0:
            return True
        else:
            return False

    def peek(self):
        if not self.isEmpty():
            return self.data[self.size()-1]
        else:
            return False

    def peekAt(self, pos):
        return self.data[pos]

    def copyTo(self):
        stack = Stack()
        for ele in self.data:
            stack.push(ele)
        return stack

    def toString(self):
        string1 = ""
        size = len(self.data)
        if size > 0:
            for i in reversed(xrange(size)):
                    string1 += str(self.data[i])
        elif size is 0:
            string1 += " "

        return string1

    def printStack(self):
        print self.data

    def contains(self, value):
        for i in range(len(self.data)):
            if self.data[i] is value:
                return i
        return -1
