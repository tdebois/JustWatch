#!/usr/bin/env python
# coding: utf-8

import os

from justwatch import WatchManager, Observer
from unittest import TextTestRunner, loader

manager = WatchManager()
manager.add_dir("./tests", only_ext=["py"])

observer = Observer(manager)


@observer.set_callback
def callback(item):

    print "Catch the modification of '{0}'".format(item.path)
    test_path = os.path.join(os.path.dirname(__file__), '../tests')
    test_loader = loader.TestLoader()
    testrunner = TextTestRunner(verbosity=2)
    testrunner.run(test_loader.discover(test_path))
    print "=" * 80


if __name__ == '__main__':

    print "--- Watch start ---"

    try:
        observer.watch()

    except KeyboardInterrupt:
        print "Bye."
