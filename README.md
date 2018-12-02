# PyContracts: A decorator-based Python contracts library

[![Build Status](https://travis-ci.org/AlexandruBurlacu/pycontracts.svg?branch=master)](https://travis-ci.org/AlexandruBurlacu/pycontracts) [![Coverage Status](https://coveralls.io/repos/github/AlexandruBurlacu/pycontracts/badge.svg?branch=master)](https://coveralls.io/github/AlexandruBurlacu/pycontracts?branch=master)

Python generally lacks type checking, and that's a problem, a very annoying one.
That's why I decided to write this small library that enables easy integration of pre- and post- conditions checking of any functions and methods.

It provides a simple, yet powerful interface, based on Python decorators and makes use of informative error messages to assist developers in debugging their systems.

This library makes it easy to specify contracts, providing defensive programming/Design by Contracts capabilities.

It has absolutely no dependencies other than Python's standard library, so it is fully compatible with both Python 3.x and 2.x, and even PyPy.

### Example

```python

from pycontracts import Contract
# You can also import some predicates (like `check_all` and `check_any`)
# and utility functions (like `drop_fst_arg`) from `pycontracts.utils`


class TestClass(object):
    # First add the constraints
    # Make sure to give a good title/key, it will help you understand, and then debug the code
    
    @Contract.pre_conditions({
        "Both arguments should be positive": lambda args: args.arg__1 > 0 and args.arg__2 > 0
    })
    def query(self, arg1, arg2):
         return arg1 * arg2


    @Contract.post_conditions({
        "Return argument should be None": lambda ret: ret is None
    })
    def command(self):
        print("It's a command, it has no return")

# Then you can run the code as usual
test_instance = TestClass()
result = test_instance.query(12, 43)
test_instance.command()

# And when everything's fine, just disable the contracts
Contract.disable_all_tests()

```

### Roadmap
- Enchance the traceback
- Publish it on PyPI
