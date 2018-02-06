#!/usr/bin/env python
# coding=utf-8


from __future__ import unicode_literals
import unittest

import httpretty

from onepiece import main


class MainTestCase(unittest.TestCase):

    def test_do_print_example(self):
        text = main.do_print_example()
        self.assertEqual(text, '海贼王（One Piece）')

    def test_do_numliterals_example(self):
        number = main.do_numliterals_example()
        self.assertEqual(number, 0o755)

    def test_do_except_example(self):
        number = main.do_except_example()
        self.assertIsNone(number)

    def test_do_raise_example(self):
        with self.assertRaises(Exception) as cm:
            main.do_raise_example()
        ex = cm.exception
        self.assertEqual(ex.args[0], 'I am Exception')

    @httpretty.activate
    def test_do_urllib_example(self):
        httpretty.register_uri(
            httpretty.GET, 'http://www.google.com', body='Fake Google',
            status=200)

        response = main.do_urllib_example()
        self.assertEqual(response.code, 200)
