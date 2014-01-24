import unittest

class TearDownAlwaysTestCase(unittest.TestCase):

    def tearDown(self):
        print
        print 'I am tearDown'

    def test_one(self):
        self.assertEqual(1, 1)
        print not_defined

    def test_two(self):
        self.assertEqual(2, 2)

if __name__ == '__main__':
    unittest.main()
