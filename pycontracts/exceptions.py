class PreconditionViolationError(Exception):
    """
    Will be raised when one of the preconditions fail.

    The error message will print the input arguments and keyword arguments
    passed to the function/method and the contract message, for example:
    ``PreconditionViolationError: First argument should be positive. [Inp]: (-10,), {}``
    """

    def __init__(self, args, kwargs, msg):
        self.message = msg
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return "{}. [Inp]: {}, {}".format(self.message, self.args, self.kwargs)

class PostconditionViolationError(Exception):
    """
    Will be raised when one of the postconditions fail.

    The error message will print the return value of
    the function/method and the contract message, for example:
    ``PostconditionViolationError: Return argument shouldn't be negative. [Out]: -10``
    """

    def __init__(self, ret_vals, msg):
        self.message = msg
        self.ret_vals = ret_vals

    def __str__(self):
        return "{}. [Out]: {}".format(self.message, self.ret_vals)
