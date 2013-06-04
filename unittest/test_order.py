import unittest

class ExampleOrderTestCase(unittest.TestCase):

    def setUp(self):
        print
        print 'I am setUp'

    def tearDown(self):
        print 'I am tearDown'

    def test_do_something(self):
        print 'I am test_do_something'

    def test_do_something_else(self):
        print 'I am test_do_something_else'

if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2))  # Python 2.6
    #unittest.main(verbosity=2)  # Python 2.7
