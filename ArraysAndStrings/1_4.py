"""
Write a method to decide if two strings are anagrams or not.
"""
import unittest


def isAnagram(string1, string2):
    string1 = string1.replace(" ", "")
    string2 = string2.replace(" ", "")
    if len(string1) != len(string2):
        return False
    checkHT = dict()
    for x in string1:
        if x == " ":
            continue
        curChar = x.lower()
        if curChar not in checkHT:
            checkHT[curChar] = 1
        else:
            checkHT[curChar] = checkHT[curChar] + 1
    for x in string2:
        if x == " ":
            continue
        curChar = x.lower()
        if curChar not in checkHT or checkHT[curChar] <= 0:
            return False
        else:
            checkHT[curChar] = checkHT[curChar] - 1
    return True


class isAnagramTest(unittest.TestCase):
    def testOne(self):
        self.assertEquals(True, isAnagram("The eyes", "They see"))

    def testTwo(self):
        self.assertEquals(True, isAnagram("Desperation", "A rope ends it"))

    def testThree(self):
        self.assertEquals(False, isAnagram("Astronome", "Moon starer"))

    def testFour(self):
        self.assertEquals(False, isAnagram("Astronomer", "Moon stare"))

if __name__ == '__main__':
    unittest.main()
