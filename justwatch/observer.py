#!/usr/bin/env python
# coding: utf-8

import sys
import time

from yaspin import yaspin
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

        spinner = yaspin(text="Watching...", color="cyan")
        try:
            spinner.start()
            self.__watch(spinner)

        except KeyboardInterrupt:
            sys.stderr.write("\nCought KeyboardInterrupt.\n")
            spinner.stop()
            sys.exit(0)
        return

    def __watch(self, spinner):

        while True:

            for index, item in enumerate(self.manager.files_container):

                new_item = FileItem(item.path)

                if item != new_item:

                    spinner.hide()
                    self.callback(new_item)
                    spinner.show()
                    self.manager.files_container[index] = new_item

            time.sleep(0.1)
