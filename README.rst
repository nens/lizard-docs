Lizard documentation
====================

.. image:: https://api.travis-ci.com/nens/lizard-docs.svg?branch=master
   :target: https://travis-ci.com/nens/lizard-docs

.. image:: https://readthedocs.com/projects/nelen-schuurmans-lizard-documentation/badge/?version=latest
   :target: https://nelen-schuurmans-lizard-documentation.readthedocs-hosted.com/en/latest/?badge=latest
   :alt: Documentation Status

Let's do it with restructuredtext/sphinx!

The documentation is automatically build on
https://nelen-schuurmans-lizard-documentation.readthedocs-hosted.com, we will
change the URL to https://docs.lizard.net later on.


Local setup
-----------

If you can run docker, you're in luck. Especially if you're working on
windows, this is the easiest option right now. You just need to run::

  $ docker-compose up

every time you want to re-generate your documentation.

On linux, pip-installing the `requirements.txt` in a virtualenv ought to work.
Once readthedocs supports pipenv, we'll switch to that. But: `docker-compose
up` is fine for you too.

Commits are automatically tested on travis:
https://travis-ci.com/nens/lizard-docs

**Windows note:** please make sure all the filenames (especially the
extensions) are lowercase. There are some funny examples in the 3Di
documentation. Reinout will probably add an automatic check to prevent such
mishaps later on.


Special commands
----------------

If the sphinx documentation tells you about a makefile: you can run those
commands from within docker, too. For example::

  $ docker-compose run builder make latexpdf


Some sphinx/restructuredtext notes
----------------------------------

You'll need to learn a bit of restructuredtext:
http://www.sphinx-doc.org/en/stable/rest.html

Special stuff, cross-references, indices etc:
http://www.sphinx-doc.org/en/stable/markup/index.html

Any questions: ask Reinout.


Making a release
----------------

Only released versions are shown publicly on readthedocs. To make a release,
install zest.releaser::

  $ pip install zest.releaser

(It is also installed inside the docker, but your git credentials won't work
in there.)

Make a release by running::

  $ fullrelease

You can normally answer all the questions with <enter>.
