"""
Write a method to replace all spaces in a string with '%20'.
"""
import unittest


def replaceSpaces1(string):
    string = string.replace(" ", "%20")
    return string


def replaceSpaces2(string):  # without using replace method
    result = []
    for c in string:
        if c == " ":
            result.append("%20")
        else:
            result.append(c)
    return "".join(result)


class replaceSpaces1Test(unittest.TestCase):
    def testOne(self):
        self.assertEquals("Hi%20Charles", replaceSpaces1("Hi Charles"))


class replaceSpaces2Test(unittest.TestCase):
    def testOne(self):
        self.assertEquals("Hi%20Charles", replaceSpaces2("Hi Charles"))


if __name__ == '__main__':
    unittest.main()
