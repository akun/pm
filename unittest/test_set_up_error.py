import unittest

class SetUpErrorTestCase(unittest.TestCase):

    def setUp(self):
        self.assertEqual(1, 2)

    def test_one(self):
        self.assertEqual(1, 2)

    def test_two(self):
        self.assertEqual(2, 1)

if __name__ == '__main__':
    unittest.main()
