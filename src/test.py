import unittest
import util

class UtilTest(unittest.TestCase):

    def testAppendEndSlash(self):
        testData = 'src/abc'
        expected = 'src/abc/'
        result = util.appendEndSlash(testData)
        self.assertEquals(expected, result)

        testData = 'src/abc/'
        expected = 'src/abc/'
        result = util.appendEndSlash(testData)
        self.assertEquals(expected, result)

    def testRemoveEndSlash(self):
        testData = 'src/abc/'
        expected = 'src/abc'
        result = util.removeEndSlash(testData)
        self.assertEquals(expected, result)

        testData = 'src/abc'
        expected = 'src/abc'
        result = util.removeEndSlash(testData)
        self.assertEquals(expected, result)

    def testAppendStartSlash(self):
        testData = 'src/abc'
        expected = '/src/abc'
        result = util.appendStartSlash(testData)
        self.assertEquals(expected, result)

        testData = '/src/abc'
        expected = '/src/abc'
        result = util.appendStartSlash(testData)
        self.assertEquals(expected, result)

    def testRemoveStartSlash(self):
        testData = '/src/abc'
        expected = 'src/abc'
        result = util.removeStartSlash(testData)
        self.assertEquals(expected, result)

        testData = 'src/abc'
        expected = 'src/abc'
        result = util.removeStartSlash(testData)
        self.assertEquals(expected, result)


if __name__ == '__main__':
    print 'test'
    suite = (unittest.TestLoader()
                 .loadTestsFromTestCase(UtilTest))
    unittest.TextTestRunner(verbosity=2).run(suite)