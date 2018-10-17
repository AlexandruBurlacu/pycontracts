from __future__ import print_function

from pycontracts import Contract

def remove_fst(dictionary):
    del dictionary["arg__0"]
    return dictionary

class TestClassBase(object):

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

class TestClassChild(TestClassBase):

    @Contract.post_conditions({
        "Return argument should be 0": lambda ret: ret == 0
    })
    def query(self, arg1, arg2):
         return arg1 * arg2 - super(TestClassChild, self).query(arg1, arg2)


if __name__ == "__main__":
    test_instance = TestClassChild()

    result = test_instance.query(12, 43)
    test_instance.command()

