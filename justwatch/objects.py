#!/usr/bin/env python
# coding: utf-8

import os

from datetime import datetime
from hashlib import sha256

ISOFORMAT = "%Y/%m/%d/ - %H:%M:%S"


class FileItem(object):
    """Class to model a file."""

    def __init__(self, path):
        """Initiate the class by the file path."""
        self.path = path

        self.stat = os.stat(path)
        self.timestamp = self.stat.st_mtime

        self.datetime = datetime.fromtimestamp(self.timestamp)
        self.modified_at = self.datetime.strftime(ISOFORMAT)

        self.hash = self._get_hash(path)

    def _get_hash(self, path):
        """Generate a hash from a path."""
        with open(path, "r") as fp:
            content = fp.read()

        return sha256(content).hexdigest()

    def __eq__(self, other):
        """Verify if a file is equal or different from another file."""
        if (self.timestamp == other.timestamp) and (self.hash == other.hash):
            return True

        else:
            return False

    def __ne__(self, other):
        """Verify if a new file is different froma another file."""
        if (self.timestamp != other.timestamp) and (self.hash != other.hash):
            return True

        else:
            return False

    def __repr__(self):
        """Return the official string representation of the object."""
        return "<FileItem path='{0}'>".format(self.path)
