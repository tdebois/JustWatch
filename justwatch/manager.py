#!/usr/bin/env python
# coding: utf-8

import os


class WatchManager(object):

    def __init__(self):

        self.files_container = []

    def add_file(self, path):

        self._check_isfile(path)
        self.files_container.append(path)

    def add_dir(self, dirpath, ignore_ext=None):

        if not os.path.isdir(dirpath):
            raise IOError("Directory not found: '{}'".format(dirpath))

        if ignore_ext and not isinstance(ignore_ext, list):
            raise TypeError("ignore_ext is only list type")

        for current, dirs, files in os.walk(dirpath):

            if current.find(".git") != -1:
                # '.git' directory is through
                continue

            current_files = map(
                (lambda _file: os.path.join(current, _file)), files)

            for _file in current_files:

                if ignore_ext:
                    ext = _file.split(".")[-1].lower()

                    if ext not in ignore_ext:
                        self.add_file(_file)

                else:
                    self.add_file(_file)

    def _check_isfile(self, path):

        if not os.path.isfile(path):
            raise IOError("File not found: '{}'".format(path))

        else:
            return True
