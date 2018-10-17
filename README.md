# Python Contracts Library

[![Build Status](https://travis-ci.org/AlexandruBurlacu/pycontracts.svg?branch=master)](https://travis-ci.org/AlexandruBurlacu/pycontracts) [![Coverage Status](https://coveralls.io/repos/github/AlexandruBurlacu/pycontracts/badge.svg?branch=master)](https://coveralls.io/github/AlexandruBurlacu/pycontracts?branch=master)

Python generally lacks type checking, and that's a problem, a very annoying one.
That's why I decided to write this small library that enables easy integration of pre- and post- conditions checking of any functions and methods.

It provides a simple, yet powerful interface, based on Python decorators and makes use of informative error messages to assist developers in debugging their systems.

This library makes it easy to specify contracts, providing defensive programming/Design by Contracts capabilities.

It has absolutely no dependencies other than Python's standard library, so it is fully compatible with both Python 3.x and 2.x, and even PyPy.

### Roadmap
- Publish it on PyPI
- Enchance the traceback
- Add an utils module with predicates to make definition of contracts easier
- Add Arguments class to unify the access to both args and kwargs
