from __future__ import print_function

# from pycontracts import Contract

class Contract(object):

    @classmethod
    def pre_conditions(cls, conditions_dict):
        def wrapper(func):            
            def __inner(*args, **kwargs):
                for condition, predicate in conditions_dict.items():
                    assert predicate(args, kwargs), condition
                return func(*args, **kwargs)
            return __inner
        return wrapper

    @classmethod
    def post_conditions(cls, conditions_dict):
        def wrapper(func):
            def __inner(*args, **kwargs):
                ret = func(*args, **kwargs)
                for condition, predicate in conditions_dict.items():
                    assert predicate(ret), condition
                return ret
            return __inner
        return wrapper

@Contract.pre_conditions({
    "First argument should be positive": lambda args, kwargs: args[0] > 0
})
@Contract.post_conditions({
    "Return argument should be negative": lambda ret: ret < 0
})
def simple_usecase(a):
    return -a


if __name__ == "__main__":
    simple_usecase(-10)
