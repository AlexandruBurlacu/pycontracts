import unittest
from pycontracts import Contract, exceptions

@Contract.pre_conditions({
    "All arguments should be positive":
        lambda args, kwargs: all(map(lambda x: 1 if x > 0 else 0,
                                        list(args) + list(kwargs.values())))
})
@Contract.post_conditions({
    "Return value should be positive": lambda ret: ret > 0
})
def testable_function(x, y):
    return x * x + y * y



@Contract.pre_conditions({
    "All arguments should be positive":
        lambda args, kwargs: all(map(lambda x: 1 if x > 0 else 0,
                                        list(args) + list(kwargs.values())))
})
@Contract.post_conditions({
    "Return value should be positive": lambda ret: ret > 0
})
def untestable_function(x, y):
    return - (x * x + y * y)



class TestContract(unittest.TestCase):
    def test_successful_contract_decorator_args(self):
        self.assertEqual(testable_function(3, 4), 3 ** 2 + 4 ** 2)

    def test_successful_contract_decorator_kwargs(self):
        self.assertEqual(testable_function(y=3, x=4), 3 ** 2 + 4 ** 2)

    def test_successful_contract_decorator_mixed(self):
        self.assertEqual(testable_function(3, y=4), 3 ** 2 + 4 ** 2)

class TestFailingContracts(unittest.TestCase):
    def test_failing_precondition_decorator_args(self):
        self.assertRaises(exceptions.PreconditionViolationError,
                            lambda: untestable_function(2, -3))

    def test_failing_postcondition_decorator_args(self):
        self.assertRaises(exceptions.PostconditionViolationError,
                            lambda: untestable_function(2, 3))

    def test_failing_precondition_decorator_kwargs(self):
        self.assertRaises(exceptions.PreconditionViolationError,
                            lambda: untestable_function(y=2, x=-3))

    def test_failing_prostcondition_decorator_kwargs(self):
        self.assertRaises(exceptions.PostconditionViolationError,
                            lambda: untestable_function(y=2, x=3))

    def test_failing_precondition_decorator_mixed(self):
        self.assertRaises(exceptions.PreconditionViolationError,
                            lambda: untestable_function(2, y=-3))

    def test_failing_prostcondition_decorator_mixed(self):
        self.assertRaises(exceptions.PostconditionViolationError,
                            lambda: untestable_function(2, y=3))
