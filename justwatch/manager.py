#!/usr/bin/env python
# coding: utf-8

import os

from justwatch.objects import FileItem


class WatchManager(object):
    """Class to manage the watcher."""

    def __init__(self):
        """Contructor to store the files to be watched."""
        self.files_container = []

    def add_file(self, path):
        """Add file from path."""
        self._check_isfile(path)
        self.files_container.append(
            FileItem(path)
        )

    def add_dir(self, dirpath, only_ext=None, ignore_ext=None):
        """Add directory (and its files) from path."""
        if not os.path.isdir(dirpath):
            raise IOError("Directory not found: '{}'".format(dirpath))

        self._validate_ext(ignore_ext, "ignore_ext")
        self._validate_ext(only_ext, "only_ext")

        for current, dirs, files in os.walk(dirpath):

            if current.find(".git") != -1:
                # '.git' directory is through
                continue

            current_files = map(
                (lambda _file: os.path.join(current, _file)), files)

            for _file in current_files:

                file_ext = _file.split(".")[-1].lower()

                if only_ext:
                    if file_ext in only_ext:
                        self.add_file(_file)

                else:

                    if ignore_ext:
                        if file_ext not in ignore_ext:
                            self.add_file(_file)

                    else:
                        self.add_file(_file)

    def _check_isfile(self, path):
        """Check if is a file pointed from the path."""
        if not os.path.isfile(path):
            raise IOError("File not found: '{}'".format(path))

        else:
            return True

    def _validate_ext(self, ext_list, ext_name):
        """Validate extension file."""
        if ext_list and not isinstance(ext_list, list):
            raise TypeError("{0} is list type only.".format(ext_name))
