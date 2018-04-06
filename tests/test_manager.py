#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase
from justwatch.manager import WatchManager


class ManagerTestCase(TestCase):

    def setUp(self):

        self.manager = WatchManager()

    def tearDown(self):

        pass

    def test_add_file(self):

        with self.assertRaises(IOError):
            self.manager.add_file("./test")

        self.manager.add_file("./README.md")

        self.assertEqual(
            self.manager.files_container,
            ["./README.md"]
        )

    def test_add_dir(self):

        with self.assertRaises(IOError):
            self.manager.add_dir("./test")

        self.manager.add_dir("./tests")

        self.assertEqual(
            self.manager.files_container,
            ["./tests/test_manager.py"]
        )
