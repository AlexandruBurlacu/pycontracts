from .exceptions import PreconditionViolationError, PostconditionViolationError
from .arguments import Arguments
from functools import wraps

class Contract(object):
    """
    Specifies through class methods the pre- and post- conditions of the contract.

    All members are classmethods, that is, to access them one doesn't need to instatiate the ``Contract`` class,
    only to apply it as a decorator, like this
    ``@Contract.pre_conditions({ <your contracts here, in the form contract_as_a_string: predicate_to_verify_the_contract/> })``.
    """

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
