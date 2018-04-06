#!/usr/bin/env python
# coding: utf-8

import os
import sys

from unittest import TextTestRunner, loader

test_path = os.path.join(os.path.dirname(__file__), 'tests')
test_loader = loader.TestLoader()

if __name__ == "__main__":

    testrunner = TextTestRunner(verbosity=2)
    test_result = testrunner.run(test_loader.discover(test_path))
    exit_code = test_result.wasSuccessful()
    sys.exit(0 if exit_code is True else 1)
