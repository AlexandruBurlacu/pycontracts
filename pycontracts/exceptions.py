import sys, traceback

class PreconditionViolationError(Exception):

    def __init__(self, args, kwargs, msg):
        self.message = msg
        self.in_args = args
        self.in_kwargs = kwargs

        super(PreconditionViolationError, self).__init__(msg)

    def __str__(self):
        return "{}. [Inp]: {}, {}".format(self.message, self.in_args, self.in_kwargs)

class PostconditionViolationError(Exception):

    def __init__(self, ret_vals, msg):
        self.message = msg
        self.ret_vals = ret_vals

        super(PostconditionViolationError, self).__init__(msg)

    def __str__(self):
        return "{}. [Out]: {}".format(self.message, self.ret_vals)
