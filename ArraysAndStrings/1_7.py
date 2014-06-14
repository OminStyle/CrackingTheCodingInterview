"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire
row and column is set to 0.
"""
import unittest


def createZeroMatix(m, n):
    return [[0 for i in range(m)] for j in range(n)]


class createZeroMatixTest(unittest.TestCase):
    def testOne(self):
        self.assertEquals([[0, 0], [0, 0], [0, 0]], createZeroMatix(2, 3))

if __name__ == '__main__':
    unittest.main()
