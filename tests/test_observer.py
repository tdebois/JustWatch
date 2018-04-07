#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase
from justwatch.manager import WatchManager
from justwatch.observer import Observer


class ManagerTestCase(TestCase):

    def setUp(self):

        self.manager = WatchManager()
        self.observer = Observer(self.manager)

    def tearDown(self):

        pass

    def test_observer(self):

        self.assertEqual(
            self.observer.manager, self.manager)

        def callback(item):
            print item.path

        self.observer.set_callback(callback)

        self.assertEqual(
            self.observer.callback, callback)
