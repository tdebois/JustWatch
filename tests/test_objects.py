#!/usr/bin/env python
# coding: utf-8

import os

from unittest import TestCase
from justwatch.objects import FileItem


class FileItemTestCase(TestCase):

    def setUp(self):

        pass

    def test_obj(self):

        path = self._setup_testenv()
        file_obj = FileItem(path)

        self.assertEqual(file_obj, FileItem(path))

        self._update(path)

        new_obj = FileItem(path)
        self.assertFalse(file_obj == new_obj)

        self._teardown_testenv(path)

    def _setup_testenv(self):

        path = "/tmp/justwatch-test"

        with open(path, "w") as fp:
            fp.write("Hello, World")

        return path

    def _update(self, path):

        with open(path, "w") as fp:
            fp.write("aaa")

    def _teardown_testenv(self, path):

        os.remove(path)
