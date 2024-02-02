Lizard documentation
====================

.. image:: https://api.travis-ci.com/nens/lizard-docs.svg?branch=master
   :target: https://travis-ci.com/nens/lizard-docs

.. image:: https://readthedocs.com/projects/nelen-schuurmans-lizard-documentation/badge/?version=latest
   :target: https://nelen-schuurmans-lizard-documentation.readthedocs-hosted.com/en/latest/?badge=latest
   :alt: Documentation Status

Let's do it with restructuredtext/sphinx!

The documentation is automatically build (as test) on github
actions. Successful builds of the **master** branch are automatically uploaded
to https://docs.lizard.net via
https://artifacts.lizard.net/overview/lizard-docs/ .


Local setup
-----------

If you can run docker, you're in luck. Especially if you're working on
windows, this is the easiest option right now. You just need to run::

  $ docker-compose up

every time you want to re-generate your documentation.

If the setup changed (which should rarely happen), a quick ``docker-compose
build`` will get you up to date.


Special commands
----------------

If the sphinx documentation tells you about a makefile: you can run those
commands from within docker, too. For example::

  $ docker-compose run builder make latexpdf

To get a really fresh build::

  $ docker-compose run builder make clean


Some sphinx/restructuredtext notes
----------------------------------

You'll need to learn a bit of restructuredtext:
http://www.sphinx-doc.org/en/stable/rest.html

Special stuff, cross-references, indices etc:
http://www.sphinx-doc.org/en/stable/markup/index.html

Any questions: ask Reinout.


Neatness notes
--------------

**Windows:** please make sure all the filenames (especially the extensions)
are lowercase. There are some funny examples in the 3Di documentation. Reinout
will probably add an automatic check to prevent such mishaps later on.

As almost everybody in Nelen & Schuurmans has write access to this repository,
the master branch has been protected. So: you must make your modifications in
a branch and merge them into master afterwards (preferrably with a pull
request). Note that the checks must pass before you can merge.


Making a release
----------------

Unlike the 3di documentation, all successful builds of **master** on travis
are uploaded as docs.lizard.net, you don't need a release for that.

For administrative purposes, making a release can be useful. To make a
release, install zest.releaser::

  $ pip install zest.releaser

Make a release by running::

  $ fullrelease

You can normally answer all the questions with <enter>.
