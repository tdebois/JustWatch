#!/usr/bin/env python
# coding: utf-8

import time

from justwatch.objects import FileItem


class Observer(object):
    """Class to model a modification observer."""
    def __init__(self, manager):
        """Initiate the class with a manager."""
        self.manager = manager
        self.callback = None

    def set_callback(self, func):
        """Set the callback by a function."""
        self.callback = func

    def watch(self):
        """Watch the file modifications."""
        while True:

            for index, item in enumerate(self.manager.files_container):

                new_item = FileItem(item.path)

                if item != new_item:

                    self.callback(new_item)
                    self.manager.files_container[index] = new_item

            time.sleep(0.1)
