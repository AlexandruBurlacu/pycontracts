from .exceptions import PreconditionViolationError, PostconditionViolationError
from .arguments import Arguments
from functools import wraps

class Contract(object):

    tests_enabled = True

    @classmethod
    def pre_conditions(cls, conditions_dict):
        def wrapper(func):
            @wraps(func)
            def __inner(*args, **kwargs):
                func_args = Arguments(*args, **kwargs)
                if cls.tests_enabled:
                    for condition, predicate in conditions_dict.items():
                        if not predicate(func_args):
                            raise PreconditionViolationError(args, kwargs, condition)
                return func(*args, **kwargs)
            return __inner
        return wrapper

    @classmethod
    def post_conditions(cls, conditions_dict):
        def wrapper(func):
            @wraps(func)
            def __inner(*args, **kwargs):
                ret = func(*args, **kwargs)
                if cls.tests_enabled:
                    for condition, predicate in conditions_dict.items():
                        if not predicate(ret):
                            raise PostconditionViolationError(ret, condition)
                return ret
            return __inner
        return wrapper

    @classmethod
    def disable_all_tests(cls):
        cls.tests_enabled = False

    @classmethod
    def enable_all_tests(cls):
        cls.tests_enabled = True
