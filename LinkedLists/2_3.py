"""
Implement an algorithm to delete a node in the middle of a single linked list,
given only access to that node.

EXAMPLE
Input: the node 'c' from the linked list a->b->c->d->e
Result: nothing is returned, but the new linked list looks like a->b->d->e
"""
import unittest


def delete(node):
    node.data = node.next.data
    node.next = node.next.next


class Node():
    def __init__(self, d):
        self.data = d
        self.next = None

    @staticmethod
    def appendToEnd(node, d):
        if node is None:
            return
        while node.next is not None:
            node = node.next
        node.next = Node(d)


class deleteTest(unittest.TestCase):
    nodeA = Node('a')
    Node.appendToEnd(nodeA, 'b')
    nodeC = Node('c')
    nodeA.next.next = nodeC
    Node.appendToEnd(nodeA, 'd')
    Node.appendToEnd(nodeA, 'e')

    def testOne(self):
        delete(self.nodeC)
        self.assertEquals('a', self.nodeA.data)
        self.assertEquals('b', self.nodeA.next.data)
        self.assertEquals('d', self.nodeA.next.next.data)
        self.assertEquals('e', self.nodeA.next.next.next.data)
        self.assertEquals(None, self.nodeA.next.next.next.next)

if __name__ == '__main__':
    unittest.main()
