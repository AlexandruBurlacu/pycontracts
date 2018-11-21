"""
PyContracts: A decorator-based Python contracts library.
========================================================

Documentation is available in the docstrings.

Contents
--------
PyContracts has no external dependencies
and is compatible with both Python 2.x and Python 3.x, and even both versions of PyPy.

Subpackages
-----------
For casual usage, it's enough to do ``from pycontracts import Contract``.
Other functionalities, like the ones from the ``utils`` package,
require explicit import, like ``from pycontracts import utils``
or ``from pycontracts.utils import check_any``.

::

arguments           --- Package for internal usage that holds the ``Arguments`` class,
                        for convenient manipulation of arguments when specifying contracts.
exceptions          --- Package for internal usage that holds the
                        ``PreconditionViolationError`` and ``PostconditionViolationError`` classes.
contract            --- User facing package that holds the ``Contract`` class,
                        used to specify the contracts on functions and methods.
utils               --- User facing package for functions that ease
                        the process of defining complex predicates for contracts.

"""

from .contract import Contract

name = "pycontracts"
__author__ = "Alex Burlacu"
__mail__ = "alexburlacu96@gmail.com"
__version__ = "0.2.1"
