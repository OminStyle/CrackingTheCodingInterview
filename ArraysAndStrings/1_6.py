"""
Given an image represented by an NxN matrix, where each pixel in the image is
4bytes, write a method to rotate the image by 90 degrees. Can you do this in
place?
"""
import unittest


def rotateImage(image):
    result = [[0 for i in range(5)] for j in range(5)]
    length = len(image)
    for i in range(length):
        for j in range(length):
            newX = j
            newY = length - i - 1
            result[newX][newY] = image[i][j]
    return result


def printArray(array):
    for i in range(len(array)):
        print array[i]
    print ""


class rotateImageTest(unittest.TestCase):
    def testOne(self):
        image = [[0 for i in range(5)] for j in range(5)]
        for i in range(5):
            image[i][0] = 1
            image[0][i] = 1
        image[1][1] = 1
        image[1][2] = 1
        rotatedThreeTimes = rotateImage(rotateImage(rotateImage(rotateImage(image))))
        self.assertEquals(image, rotatedThreeTimes)

if __name__ == "__main__":
    unittest.main()

"""
image = [[0 for i in range(5)] for j in range(5)]
for i in range(5):
    image[i][0] = 1
    image[0][i] = 1
image[1][1] = 1
image[1][2] = 1
printArray(image)
image1 = rotateImage(rotateImage(rotateImage(rotateImage(image))))
printArray(image1)
"""
