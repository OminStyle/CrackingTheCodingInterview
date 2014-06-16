"""
Implement an algorithm to find the nth to last element of a singly linked list.
"""
import unittest


class Node:

    def __init__(self, d):
        self.next = None
        self.data = d

    def appendToEnd(self, d):
        node = self
        while node.next is not None:
            node = node.next
        node.next = Node(d)


def nthToLastElement(head, nth):
    runner = head
    length = 1
    while runner.next is not None:
        runner = runner.next
        length += 1
    runner = head
    for i in range(length-nth-1):
        runner = runner.next
    return runner.data


class NthToLastElementTest(unittest.TestCase):
    # 5-4-3-2-1-0
    head = Node(5)
    head.appendToEnd(4)
    head.appendToEnd(3)
    head.appendToEnd(2)
    head.appendToEnd(1)
    head.appendToEnd(0)

    def testOne(self):
        self.assertEquals(3, nthToLastElement(self.head, 3))

    def testTwo(self):
        self.assertNotEquals(2, nthToLastElement(self.head, 3))

if __name__ == '__main__':
    unittest.main()
