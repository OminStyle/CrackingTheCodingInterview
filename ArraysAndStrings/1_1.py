"""
Implement an algorithm to determine if a string has all unique characters.
What if you can not use additional data structures
"""
import unittest


def isUnique(myString):
    myUniquenessArray = [False] * 256
    for x in myString:
        if myUniquenessArray[ord(x)] is False:
            myUniquenessArray[ord(x)] = True
        else:
            print "Your string is includes non-unique character(s)."
            return False
    print "Your string has all unique characters."
    return True


class isUniqueTest(unittest.TestCase):
    def testOne(self):
        self.assertEquals(True, isUnique("ADF!@#jv."))

    def testTwo(self):
        self.assertEquals(False, isUnique(" ASDF@#F.~% "))

if __name__ == '__main__':
    unittest.main()

# User Interaction
"""
print "I will determine if your string has all unique characters."
print "Type in your string: ",
myString = raw_input()
isUnique(myString)
"""
