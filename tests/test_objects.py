#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase
from justwatch.objects import FileItem


class FileItemTestCase(TestCase):

    def setUp(self):

        pass

    def test_obj(self):

        testcase = "/tmp/justwatch-test"
        with open(testcase, "w") as fp:
            fp.write("aaa")

        a = FileItem(testcase)
        b = FileItem(testcase)

        self.assertEqual(a, b)
        self.assertTrue(a == b)

        with open(testcase, "w") as fp:
            fp.write("bbb")

        c = FileItem(testcase)

        self.assertNotEqual(a, c)
        self.assertFalse(a == c)
