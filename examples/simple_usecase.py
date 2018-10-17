from __future__ import print_function

from pycontracts import Contract

@Contract.pre_conditions({
    "First argument should be positive": lambda args, kwargs: args[0] > 0
})
@Contract.post_conditions({
    "Return argument should be negative": lambda ret: ret < 0
})
def simple_usecase(a):
    return -a


if __name__ == "__main__":
    Contract.disable_all_tests()
    simple_usecase(-10)
    Contract.enable_all_tests()
    simple_usecase(10)
