import unittest
from pycontracts import Contract, utils


@Contract.pre_conditions({
    "All arguments should be positive":
        lambda args: utils.check_all(args.all_args, lambda arg: arg > 0)
})
@Contract.post_conditions({
    "Return value should be positive": lambda ret: ret[0] > 0 and ret[1] > 0
})
def untestable_function(x, y, z, w):
    return - (x * x + y * y), (z + w)


class TestDisabledContracts(unittest.TestCase):

    def setUp(self):
        Contract.disable_all_tests()

    def test_not_failing_precondition_decorator_mixed(self):
        self.assertEqual(untestable_function(2, 3, z=4, w=-3), (-13, 1))

    def test_not_failing_postcondition_decorator_mixed(self):
        self.assertEqual(untestable_function(2, 3, z=4, w=-3), (-13, 1))

    def tearDown(self):
        Contract.enable_all_tests()
