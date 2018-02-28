#!/usr/bin/env python
# coding=utf-8


from unittest import TestCase

from onepiece.example import hello_world


class HelloWordTestCase(TestCase):

    def test_hello_world(self):
        self.assertEqual('One Piece', hello_world())
