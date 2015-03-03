ExquisiteCorpse
===============
A microgame runner.

[![Build Status](http://img.shields.io/travis/GamedevGR/exquisite-corpse/master.svg)](https://travis-ci.org/GamedevGR/exquisite-corpse)
[![Coverage Status](http://img.shields.io/coveralls/GamedevGR/exquisite-corpse/master.svg)](https://coveralls.io/r/GamedevGR/exquisite-corpse)
[![Scrutinizer Code Quality](http://img.shields.io/scrutinizer/g/GamedevGR/exquisite-corpse.svg)](https://scrutinizer-ci.com/g/GamedevGR/exquisite-corpse/?branch=master)
[![PyPI Version](http://img.shields.io/pypi/v/ExquisiteCorpse.svg)](https://pypi.python.org/pypi/ExquisiteCorpse)
[![PyPI Downloads](http://img.shields.io/pypi/dm/ExquisiteCorpse.svg)](https://pypi.python.org/pypi/ExquisiteCorpse)


Getting Started
===============

Requirements
------------

* Python 3.3+

Installation
------------

ExquisiteCorpse can be installed with pip:

```
$ pip install ExquisiteCorpse
```

or directly from the source code:

```
$ git clone https://github.com/gamedevgr/exquisite-corpse.git
$ cd exquisite-corpse
$ python setup.py install
```

Basic Usage
===========

After installation, the package can imported:

```
$ python
>>> import ec
>>> ec.__version__
```

ExquisiteCorpse doesn't do anything yet.

For Contributors
================

Requirements
------------

* Make:
    * Windows: http://cygwin.com/install.html
    * Mac: https://developer.apple.com/xcode
    * Linux: http://www.gnu.org/software/make (likely already installed)
* virtualenv: https://pypi.python.org/pypi/virtualenv#installation
* Pandoc: http://johnmacfarlane.net/pandoc/installing.html
* Graphviz: http://www.graphviz.org/Download.php

Installation
------------

Create a virtualenv:

```
$ make env
```

Run the tests:

```
$ make test
$ make tests  # includes integration tests
```

Build the documentation:

```
$ make doc
```

Run static analysis:

```
$ make pep8
$ make pep257
$ make pylint
$ make check  # includes all checks
```

Prepare a release:

```
$ make dist  # dry run
$ make upload
```
