from exceptions import PreconditionViolationError, PostconditionViolationError

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
