from __future__ import print_function

# from pycontracts import Contract

class PreconditionViolationError(Exception):

    def __init__(self, predicate, args, kwargs, msg):
        self.message = msg
        self.args = args
        self.kwargs = kwargs
        self.predicate = predicate

    def __str__(self):
        return "{}. [Inp]: {}, {}".format(self.message, self.args, self.kwargs)

class PostconditionViolationError(Exception):

    def __init__(self, predicate, ret_vals, msg):
        self.message = msg
        self.ret_vals = ret_vals
        self.predicate = predicate

    def __str__(self):
        return "{}. [Out]: {}".format(self.message, self.ret_vals)


class Contract(object):

    @classmethod
    def pre_conditions(cls, conditions_dict):
        def wrapper(func):            
            def __inner(*args, **kwargs):
                for condition, predicate in conditions_dict.items():
                    raise PreconditionViolationError(predicate, args, kwargs, condition)
                return func(*args, **kwargs)
            return __inner
        return wrapper

    @classmethod
    def post_conditions(cls, conditions_dict):
        def wrapper(func):
            def __inner(*args, **kwargs):
                ret = func(*args, **kwargs)
                for condition, predicate in conditions_dict.items():
                    raise PostconditionViolationError(predicate, ret, condition)
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
