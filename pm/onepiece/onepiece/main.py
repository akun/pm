#!/usr/bin/env python
# coding=utf-8


from __future__ import print_function, unicode_literals

from future import standard_library
standard_library.install_aliases()

import urllib.request


def do_print_example():
    text = '海贼王（One Piece）'
    print(text)
    return text


def do_numliterals_example():
    number = 0o755
    return number


def do_except_example():
    try:
        number = 1 / 0
    except ZeroDivisionError as ex:
        number = None
    return number


def do_raise_example():
    raise Exception('I am Exception')


def do_urllib_example():
    response = urllib.request.urlopen('http://www.google.com')
    return response
