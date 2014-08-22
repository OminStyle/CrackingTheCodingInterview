"""
How would you design a stack which, in addition to push and pop, also has a
function min which returns the minimum element? Push, pop and min should all
operate in O(1) time.
"""
import unittest
from stack import Stack
from node import Node


class StackExtended(Stack):
    def __init__(self):
        self.minStack = Stack()
        super(StackExtended, self).__init__()

    def push(self, item):
        if self.getMin() is None:
            self.minStack.push(item)
        elif item <= self.getMin():
            self.minStack.push(item)
        super(StackExtended, self).push(item)

    def pop(self):
        popped = super(StackExtended, self).pop()
        if popped == self.getMin():
            self.minStack.pop()
        return popped

    def getMin(self):
        if self.minStack.peek() is None:
            return None
        return self.minStack.peek().data


class StackExtendedTest(unittest.TestCase):
    def testOne(self):
        stack = StackExtended()
        stack.push(3)
        stack.push(2)
        stack.push(2)
        stack.push(1)
        self.assertEquals(1, stack.getMin())
        stack.pop()
        self.assertEquals(2, stack.getMin())
        stack.pop()
        self.assertEquals(2, stack.getMin())

if __name__ == "__main__":
    unittest.main()
