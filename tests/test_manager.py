#!/usr/bin/env python
# coding: utf-8

import os
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

        testcase = "./tests"
        self.manager.add_dir(testcase)

        files = os.listdir(testcase)
        add_dir_result = map(
            (lambda _file: os.path.join(testcase, _file)), files)

        self.assertEqual(
            self.manager.files_container,
            add_dir_result
        )

    def test_add_dir_with_ignore(self):

        testcase = "./tests"

        with self.assertRaises(TypeError):
            self.manager.add_dir(testcase, ignore_ext="swp")

        self.manager.add_dir(testcase, ignore_ext=["swp"])

        files = os.listdir(testcase)
        add_dir_result = map(
            (lambda _file: os.path.join(testcase, _file)),
            [_file for _file in files if not _file.endswith("swp")])

        self.assertEqual(
            self.manager.files_container,
            add_dir_result
        )
