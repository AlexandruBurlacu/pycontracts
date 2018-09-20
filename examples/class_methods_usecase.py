from __future__ import print_function

from pycontracts import Contract


class TestClass(object):

    @Contract.pre_conditions({
        "Both arguments should be positive": lambda args, kwargs: args[0] > 0 and args[1] > 0
    })
    def query(self, arg1, arg2):
         return arg1 * arg2


    @Contract.post_conditions({
        "Return argument should be None": lambda ret: ret is None
    })
    def command(self):
        print("It's a command, it has no return")


if __name__ == "__main__":
    test_instance = TestClass()

    result = test_instance.query(12, 43)
    test_instance.command()

