class PreconditionViolationError(Exception):

    def __init__(self, args, kwargs, msg):
        self.message = msg
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return "{}. [Inp]: {}, {}".format(self.message, self.args, self.kwargs)

class PostconditionViolationError(Exception):

    def __init__(self, ret_vals, msg):
        self.message = msg
        self.ret_vals = ret_vals

    def __str__(self):
        return "{}. [Out]: {}".format(self.message, self.ret_vals)
