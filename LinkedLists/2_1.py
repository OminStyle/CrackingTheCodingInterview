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
    def removeDuplicates(head):
        uniqueData = dict()
        uniqueData[head.data] = True
        node = head
        while node.next is not None:
            if node.next.data in uniqueData:
                node.next = node.next.next
            else:
                uniqueData[node.next.data] = True
                node = node.next

    @staticmethod
    def removeDuplicates1(head):
        while head.next is not None:
            runner = head
            while runner.next is not None:
                if head.data == runner.next.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            head = head.next


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

    def testTwo(self):
        node = Node(1)
        node.appendToTail(2)
        node.appendToTail(2)
        node.appendToTail(2)
        node.appendToTail(2)
        node.appendToTail(3)
        node.appendToTail(2)
        node.appendToTail(1)
        Node.removeDuplicates1(node)
        self.assertEquals(1, node.data)
        node = node.next
        self.assertEquals(2, node.data)
        node = node.next
        self.assertEquals(3, node.data)
        node = node.next
        self.assertEquals(None, node)

if __name__ == '__main__':
    unittest.main()
