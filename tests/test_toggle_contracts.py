import unittest
from pycontracts import Contract


@Contract.pre_conditions({
    "All arguments should be positive":
        lambda args: all(map(lambda x: 1 if x > 0 else 0, list(args.all_args.values())))
})
@Contract.post_conditions({
    "Return value should be positive": lambda ret: ret > 0
})
def untestable_function(x, y):
    return - (x * x + y * y)


class TestDisabledContracts(unittest.TestCase):

    def setUp(self):
        Contract.disable_all_tests()

    def test_not_failing_precondition_decorator_mixed(self):
        self.assertEqual(untestable_function(2, y=-3), -13)

    def test_not_failing_prostcondition_decorator_mixed(self):
        self.assertEqual(untestable_function(2, y=3), -13)

    def tearDown(self):
        Contract.enable_all_tests()
