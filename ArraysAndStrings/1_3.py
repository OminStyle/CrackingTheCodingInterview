"""
Design an algorithm and write code to remove the duplicate characters in a
string without using any additional buffer. NOTE: One or two additional
varaibles are fine. An extra copy of the array is not.

FOLLOW UP
Write the test cases for this method
"""
import unittest


def removeDupChars(myString):
    result = ""
    for x in myString:
        isDup = False
        for y in result:
            if y is x:
                isDup = True
                break
        if isDup is False:
            result = result + x
        isDup = True
    return result


class removeDupCharsTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual("abc", removeDupChars("aabbcc"))

    def testTwo(self):
        self.assertEqual("abc", removeDupChars("abc"))

    def testThree(self):
        self.assertEqual("ab", removeDupChars("aaabaaaabbababab"))

if __name__ == '__main__':
    unittest.main()
