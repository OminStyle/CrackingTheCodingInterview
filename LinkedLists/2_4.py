"""
You have two numbers represented by a linked list, where each node contains a
single digit. The digits are stored in reverse order, such that the 1's digit
is at the head of the list. Write a function that adds the two numbers and
returns the sum as a linked list.

EXAMPLE
Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
Output: 8 -> 0 -> 8
"""
import unittest


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def appendToEnd(self, newNode):
        node = self.head
        if node is None:
            self.head = newNode
        else:
            while node.next is not None:
                node = node.next
            node.next = newNode
        self.length += 1

    @staticmethod
    def sumOfTwoNumbers(num1, num2):
        newLL = LinkedList()
        carry = 0
        if num1.length >= num2.length:
            node1 = num1.head
            node2 = num2.head
        else:
            node1 = num2.head
            node2 = num1.head
        while node1 is not None:
            newNode = 0
            if node2 is not None:
                newNode = Node(node1.data + node2.data + carry)
                node1 = node1.next
                node2 = node2.next
                carry = 0
            else:
                newNode = Node(node1.data + carry)
                node1 = node1.next
                carry = 0
            newLL.appendToEnd(newNode)
            if newNode.data >= 10:
                newNode.data -= 10
                carry = 1
        return newLL


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class sumOfTwoNumberTest(unittest.TestCase):
    num1 = LinkedList()
    num1.appendToEnd(Node(3))
    num1.appendToEnd(Node(1))
    num1.appendToEnd(Node(5))

    num2 = LinkedList()
    num2.appendToEnd(Node(5))
    num2.appendToEnd(Node(9))
    num2.appendToEnd(Node(2))

    def testOne(self):
        n1 = self.num1
        n2 = self.num2
        self.assertEquals(3, n1.length)
        self.assertEquals(3, n2.length)

        self.assertEquals(3, n1.head.data)
        self.assertEquals(1, n1.head.next.data)
        self.assertEquals(5, n1.head.next.next.data)

        self.assertEquals(5, n2.head.data)
        self.assertEquals(9, n2.head.next.data)
        self.assertEquals(2, n2.head.next.next.data)

    def testTwo(self):
        n1 = self.num1
        n2 = self.num2
        nSum = LinkedList.sumOfTwoNumbers(n1, n2)
        head = nSum.head
        self.assertEquals(8, head.data)
        self.assertEquals(0, head.next.data)
        self.assertEquals(8, head.next.next.data)

if __name__ == '__main__':
    unittest.main()
