"""
Given a circular linked list, implement an algorithm which returns node at the
beginning of the loop.

DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer
points to an earlier node, so as to make a loop in the linked list.

EXAMPLE
input: A -> B -> C -> D -> E -> C [the same C as earlier]
output: C
"""
import unittest


def startOfLoop(head):
    n1 = head
    n2 = head

    while n2.next is not None:
        n1 = n1.next
        n2 = n2.next.next
        if n1 == n2:
            break
    if n2.next is None:
        return None
    n1 = head
    print '1'
    while n1 != n2:
        n1 = n1.next
        n2 = n2.next
    return n1.data


class Node:
    def __init__(self, d):
        self.next = None
        self.data = d

    def appendToEnd(self, nextNode):
        if nextNode is None:
            return
        while self.next is not None:
            self = self.next
        self.next = nextNode


class startOfLoopTest(unittest.TestCase):
    head = Node('A')
    head.appendToEnd(Node('B'))
    nodeC = Node('C')
    head.appendToEnd(nodeC)
    head.appendToEnd(Node('D'))
    nodeE = Node('E')
    head.appendToEnd(nodeE)
    nodeE.next = nodeC

    def testOne(self):
        head = self.head
        self.assertEquals('A', head.data)
        self.assertEquals('B', head.next.data)
        self.assertEquals('C', head.next.next.data)
        self.assertEquals('D', head.next.next.next.data)
        self.assertEquals('E', head.next.next.next.next.data)

    def testTwo(self):
        head = self.head
        self.assertEquals('C', startOfLoop(head))

if __name__ == '__main__':
    unittest.main()
