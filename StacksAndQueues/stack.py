import unittest
from node import Node


class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        if self.top is not None:
            item = self.top.data
            self.top = self.top.next
            return item
        return null

    def push(self, item):
        t = Node(item)
        if self.top is not None:
            t.next = self.top
        self.top = t


class StackTest(unittest.TestCase):
    def testOne(self):
        stack = Stack()
        stack.push('A')
        stack.push('B')
        stack.push('C')
        self.assertEquals('C', stack.pop())
        self.assertEquals('B', stack.pop())
        self.assertEquals('A', stack.pop())

if __name__ == '__main__':
    unittest.main()
