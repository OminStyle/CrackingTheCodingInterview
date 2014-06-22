import unittest
from node Import Node


class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, item):
        if self.front is None:
            self.back = Node(item)
            self.front = self.back
        else:
            self.back.next = Node(item)
            self.back = self.back.next

    def dequeue(node):
        if self.front is not None:
            item = self.front.data
            front = self.front.next
            return item
        return None


class QueueTest(unittest.TestCase):
    def testOne(self):
        stack = Queue()
        stack.enqueue('A')
        stack.enqueue('B')
        stack.enqueue('C')
        self.assertEquals('A', stack.dequeue())
        self.assertEquals('B', stack.dequeue())
        self.assertEquals('Cpy', stack.dequeue())

if __name__ == '__main__':
    unittest.main()
