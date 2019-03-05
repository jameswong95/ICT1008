class Stack:

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
        return self.data.pop()

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def peek(self):
        if not self.isEmpty():
            return self.data[self.size()-1]

    def peekAt(self,pos):
        return self.data(pos)

    def copyTo(self):
        stack = Stack()
        for ele in self.data:
            stack.push(ele)
        return stack

    def toString(self):
        string1 = ""
        for i in range(len(self._data)):
            string1 += str(self._data[i])+ " "
        return string1

    def printStack(self):
        print self._data