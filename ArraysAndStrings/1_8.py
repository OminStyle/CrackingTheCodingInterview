"""
Assume you have a method isSubstring which checks if one word is a substring of
another. Given two strings, s1 and s2, write code to check if s2 is a rotation
of s1 using only one call to isSubstring (i.e., "waterbottle" is a rotation of
"erbottlewat").
"""
import unittest


def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = s1 + s1
    if s2 in s1:
        return True
    return False


class isRotationTest(unittest.TestCase):
    def testOne(self):
        self.assertEquals(True, isRotation("waterbottle", "erbottlewat"))

    def testTwo(self):
        self.assertEquals(False, isRotation("water", "watera"))

    def testThree(self):
        self.assertEquals(False, isRotation("water", "weart"))

if __name__ == "__main__":
    unittest.main()
