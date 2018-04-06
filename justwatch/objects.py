#!/usr/bin/env python
# coding: utf-8

import os

from datetime import datetime
from hashlib import sha256

ISOFORMAT = "%Y/%m/%d/ - %H:%M:%S"


class FileItem(object):

    def __init__(self, path):

        self.path = path

        self.stat = os.stat(path)
        self.timestamp = self.stat.st_mtime

        self.datetime = datetime.fromtimestamp(self.timestamp)
        self.modified_at = self.datetime.strftime(ISOFORMAT)

        self.hash = self._get_hash(path)

    def _get_hash(self, path):

        with open(path, "r") as fp:
            content = fp.read()

        return sha256(content).hexdigest()

    def __eq__(self, other):

        if (self.timestamp == other.timestamp) and (self.hash == other.hash):
            return True

        else:
            return False

    def __ne__(self, other):

        if (self.timestamp != other.timestamp) and (self.hash != other.hash):
            return True

        else:
            return False

    def __repr__(self):

        return "<FileItem path='{0}'>".format(self.path)
