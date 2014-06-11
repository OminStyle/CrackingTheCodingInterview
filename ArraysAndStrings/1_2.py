"""
Write code to reverse a C-Style String. (C-String means that "abcd is
represented as five characters, including the null character.")
"""
import unittest


def revertString(myString):
    stringBuilder = ""
    for x in myString:
        if x is None:
            continue
        else:
            stringBuilder = x + stringBuilder
    return stringBuilder


class revertStringTest(unittest.TestCase):
    def testOne(self):
        self.assertEquals("dcba", revertString("abcd"))

    def testTwo(self):
        self.assertEquals(" cba", revertString("abc "))

if __name__ == '__main__':
    unittest.main()

# User Interaction
"""
print "I will revert your string"
print "Type in your string:",
myString = raw_input()
print revertString(myString)
"""
