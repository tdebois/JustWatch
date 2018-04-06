#!/usr/bin/env python
# coding: utf-8

import os
from unittest import TestCase
from justwatch.manager import WatchManager
from justwatch.objects import FileItem


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
            [FileItem("./README.md")]
        )

    def test_add_dir(self):

        with self.assertRaises(IOError):
            self.manager.add_dir("./test")

        testcase = "./tests"
        self.manager.add_dir(testcase)

        files = os.listdir(testcase)
        add_dir_result = map(
            (lambda _file: FileItem(os.path.join(testcase, _file))), files)

        self.assertEqual(
            self.manager.files_container,
            add_dir_result
        )

    def test_add_dir_with_ignore(self):

        testcase = "./tests"
        testext = "swp"

        with self.assertRaises(TypeError):
            self.manager.add_dir(testcase, ignore_ext=testext)

        self.manager.add_dir(testcase, ignore_ext=[testext])

        files = os.listdir(testcase)
        add_dir_result = map(
            (lambda _file: FileItem(os.path.join(testcase, _file))),
            [_file for _file in files if not _file.endswith(testext)])

        self.assertEqual(
            self.manager.files_container,
            add_dir_result
        )

    def test_add_dir_with_only(self):

        testcase = "./tests"
        testext = "py"

        with self.assertRaises(TypeError):
            self.manager.add_dir(testcase, only_ext=testext)

        self.manager.add_dir(testcase, only_ext=[testext])

        files = os.listdir(testcase)
        add_dir_result = map(
            (lambda _file: FileItem(os.path.join(testcase, _file))),
            [_file for _file in files if _file.endswith(testext)])

        self.assertEqual(
            self.manager.files_container,
            add_dir_result
        )
