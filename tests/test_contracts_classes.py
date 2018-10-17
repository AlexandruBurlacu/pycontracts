import unittest
from pycontracts import Contract, exceptions, utils

class TestClassBase(object):

    @Contract.pre_conditions({
        "All arguments should be positive":
            lambda args: utils.check_all(utils.drop_fst_arg(args.all_args), lambda arg: arg > 0)
    })
    def query(self, arg1, arg2):
         return arg1 * arg2


class TestClassChild(TestClassBase):

    @Contract.post_conditions({
        "Return argument should be 0": lambda ret: ret == 0
    })
    def query(self, arg1, arg2):
         return arg1 * arg2 + super(TestClassChild, self).query(arg1, arg2)

class TestContractSimpleClass(unittest.TestCase):

    def setUp(self):
        self.base_class_instance = TestClassBase()
        self.child_class_instance = TestClassChild()

    def test_successful_contract_decorator_args(self):
        self.assertEqual(self.base_class_instance.query(3, 4), 3 * 4)

    def test_successful_contract_decorator_kwargs(self):
        self.assertEqual(self.base_class_instance.query(arg2=3, arg1=4), 3 * 4)

    def test_successful_contract_decorator_mixed(self):
        self.assertEqual(self.base_class_instance.query(3, arg2=4), 3 * 4)

    def tearDown(self):
        del self.base_class_instance
        del self.child_class_instance

class TestFailingContractClass(unittest.TestCase):

    def setUp(self):
        self.base_class_instance = TestClassBase()
        self.child_class_instance = TestClassChild()

    def test_failing_precondition_decorator_args(self):
        self.assertRaises(exceptions.PreconditionViolationError,
                            lambda: self.base_class_instance.query(2, -3))

    def test_failing_postcondition_decorator_args(self):
        self.assertRaises(exceptions.PostconditionViolationError,
                            lambda: self.child_class_instance.query(2, 3))

    def test_failing_precondition_decorator_kwargs(self):
        self.assertRaises(exceptions.PreconditionViolationError,
                            lambda: self.base_class_instance.query(arg2=2, arg1=-3))

    def test_failing_postcondition_decorator_kwargs(self):
        self.assertRaises(exceptions.PostconditionViolationError,
                            lambda: self.child_class_instance.query(arg2=2, arg1=3))

    def test_failing_precondition_decorator_mixed(self):
        self.assertRaises(exceptions.PreconditionViolationError,
                            lambda: self.base_class_instance.query(2, arg2=-3))

    def test_failing_postcondition_decorator_mixed(self):
        self.assertRaises(exceptions.PostconditionViolationError,
                            lambda: self.child_class_instance.query(2, arg2=3))

    def tearDown(self):
        del self.base_class_instance
        del self.child_class_instance
