#-*- encoding: UTF-8 -*-


import unittest


class ExampleTestCase(unittest.TestCase):

    def test_do_somthing(self):
        self.assertEqual(1, 1)

    def test_do_somthing_else(self):
        self.assertEqual(1, 1)


class AnoterExampleTestCase(unittest.TestCase):

    def test_do_somthing(self):
        self.assertEqual(1, 1)

    def test_do_somthing_else(self):
        self.assertEqual(1, 1)


def suite_use_make_suite():
    """想把TestCase下的所有测试加到TestSuite的时候可以这样用

    """

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ExampleTestCase))
    return suite

def suite_add_one_test():
    """想把TestCase下的某个测试加到TestSuite的时候可以这样用

    """

    suite = unittest.TestSuite()
    suite.addTest(ExampleTestCase('test_do_somthing'))
    return suite

def suite_use_test_loader():
    """想用TestLoader方式把测试加到TestSuite的死后可以这样用

    """

    test_cases = (ExampleTestCase, AnoterExampleTestCase)
    suite = unittest.TestSuite()
    for test_case in test_cases:
        tests = unittest.defaultTestLoader.loadTestsFromTestCase(test_case)
        suite.addTests(tests)
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite_use_test_loader')
