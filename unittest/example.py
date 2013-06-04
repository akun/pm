import unittest

class Example3TestCase(unittest.TestCase):

    def setUp(self):
        print
        print 'I am setUp'
        print a

    def tearDown(self):
        print 'I am tearDown'

    def test_one(self):
        self.assertEqual(1, 1)

    def test_two(self):
        self.assertEqual(2, 2)

if __name__ == '__main__':
    unittest.main()
