#!/usr/bin/env python
# coding: utf-8

import os
import time

from unittest import TestCase
from justwatch.objects import FileItem


class FileItemTestCase(TestCase):

    def setUp(self):

        pass

    def test_obj(self):

        path = self._setup_testenv()
        file_obj = FileItem(path)
        new_obj = FileItem(path)

        self.assertEqual(
            repr(file_obj),
            "<FileItem path='{0}'>".format(path)
        )

        self.assertTrue(file_obj == new_obj)

        path = self._update(path)
        time.sleep(0.3)
        new_obj = FileItem(path)

        self.assertTrue(file_obj != new_obj)

        self._teardown_testenv(path)

    def _setup_testenv(self):

        path = "/tmp/justwatch-test"

        with open(path, "w") as fp:
            fp.write("Hello, World")

        return path

    def _update(self, path):

        with open(path, "w") as fp:
            fp.write("aaa")

        return path

    def _teardown_testenv(self, path):

        os.remove(path)
