JustWatch
=========

|forthebadge|

|Build Status| |Coverage Status|

📄 Overview
---------------------------

Python utility to watch the **file modification**. There are similar
libraries: `pyinotify <https://github.com/seb-m/pyinotify>`__,
`watchdog <https://github.com/gorakhargosh/watchdog>`__. These libraries
watch the file system event, but JustWatch is supported modification **only**.

✏️ Usage
---------------

quick start
~~~~~~~~~~~

First of all, import classes from ``justwatch``:

.. code:: python

    from justwatch import WatchManager, Observer

make ``WatchManager`` instance and add file or directory:

.. code:: python

    manager = WatchManager()
    manager.add_file("./README.md")
    manager.add_dir("./tests")

make ``Observer`` instance and set callback:

.. code:: python

    observer = Observer(manager)

    @observer.set_callback
    def callback(item):
        print "Catch the modification of '{0}'".format(item.path)

and run ``observer.watch``

.. code:: python

    observer.watch()

example
~~~~~~~

📥 Installation
--------------------------

::

    $ git clone git@github.com:alice1017/JustWatch.git
    $ cd JustWatch
    $ python setup.py build install

TODO: I will upload pypi registry.

👀 Contribution
-------------------

1. Forks on `Github <https://github.com/alice1017/JustWatch>`__
2. Find a bug? Send a pull request to get it merged and published.

.. |forthebadge| image:: http://forthebadge.com/images/badges/made-with-python.svg
   :target: http://forthebadge.com
.. |Build Status| image:: https://travis-ci.org/alice1017/JustWatch.svg?branch=master
   :target: https://travis-ci.org/alice1017/JustWatch
.. |Coverage Status| image:: https://coveralls.io/repos/github/alice1017/JustWatch/badge.svg
   :target: https://coveralls.io/github/alice1017/JustWatch
