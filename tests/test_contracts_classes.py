import unittest
from pycontracts import Contract, exceptions

class TestClassBase(object):

    @Contract.pre_conditions({
        "All arguments should be positive": lambda args, kwargs: all(map(lambda x: 1 if x > 0 else 0, list(args[1:]) + list(kwargs.values())))
    })
    def query(self, arg1, arg2):
         return arg1 * arg2


class TestClassChild(TestClassBase):

    @Contract.post_conditions({
        "Return argument should be 0": lambda ret: ret == 0
    })
    def query(self, arg1, arg2):
         return arg1 * arg2 + super().query(arg1, arg2)

base_class_instance = TestClassBase()
child_class_instance = TestClassChild()

class TestContractSimpleClass(unittest.TestCase):

    def test_successful_contract_decorator_args(self):
        self.assertEqual(base_class_instance.query(3, 4), 3 * 4)

    def test_successful_contract_decorator_kwargs(self):
        self.assertEqual(base_class_instance.query(arg2=3, arg1=4), 3 * 4)

    def test_successful_contract_decorator_mixed(self):
        self.assertEqual(base_class_instance.query(3, arg2=4), 3 * 4)

class TestFailingContractClass(unittest.TestCase):
    def test_failing_precondition_decorator_args(self):
        self.assertRaises(exceptions.PreconditionViolationError, lambda: base_class_instance.query(2, -3))

    def test_failing_postcondition_decorator_args(self):
        self.assertRaises(exceptions.PostconditionViolationError, lambda: child_class_instance.query(2, 3))

    def test_failing_precondition_decorator_kwargs(self):
        self.assertRaises(exceptions.PreconditionViolationError, lambda: base_class_instance.query(arg2=2, arg1=-3))

    def test_failing_prostcondition_decorator_kwargs(self):
        self.assertRaises(exceptions.PostconditionViolationError, lambda: child_class_instance.query(arg2=2, arg1=3))

    def test_failing_precondition_decorator_mixed(self):
        self.assertRaises(exceptions.PreconditionViolationError, lambda: base_class_instance.query(2, arg2=-3))

    def test_failing_prostcondition_decorator_mixed(self):
        self.assertRaises(exceptions.PostconditionViolationError, lambda: child_class_instance.query(2, arg2=3))
