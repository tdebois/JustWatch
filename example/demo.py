#!/usr/bin/env python
# coding: utf-8

from justwatch import WatchManager, Observer

manager = WatchManager()
manager.add_file("./README.md")

observer = Observer(manager)


@observer.set_callback
def callback(item):

    print "Catch the modification of '{0}'".format(item.path)
    print "  * modified at: {0}".format(item.modified_at)
    print "  * file hash: {0}".format(item.hash)


if __name__ == '__main__':

    print "--- Watch start ---"

    try:
        observer.watch()

    except KeyboardInterrupt:
        print "Bye."
