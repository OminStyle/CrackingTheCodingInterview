"""
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""
import unittest


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def appendToTail(self, d):
        n = self
        while n.next is not None:
            n = n.next
        n.next = Node(d)

    @staticmethod
    def removeDuplicates(root):
        uniqueData = dict()
        uniqueData[root.data] = True
        node = root
        while node.next is not None:
            if node.next.data in uniqueData:
                node.next = node.next.next
            else:
                uniqueData[node.next.data] = True
                node = node.next


class removeDuplicatesTest(unittest.TestCase):
    def testOne(self):
        node = Node(1)
        node.appendToTail(2)
        node.appendToTail(2)
        node.appendToTail(2)
        node.appendToTail(2)
        node.appendToTail(3)
        node.appendToTail(2)
        node.appendToTail(1)
        Node.removeDuplicates(node)
        self.assertEquals(1, node.data)
        node = node.next
        self.assertEquals(2, node.data)
        node = node.next
        self.assertEquals(3, node.data)
        node = node.next
        self.assertEquals(None, node)

if __name__ == '__main__':
    unittest.main()
