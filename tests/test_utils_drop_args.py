import unittest
from pycontracts import Contract, utils


@Contract.pre_conditions({
    "All but 'w'/last argument should be positive":
        lambda args: utils.check_all(utils.drop_args(args.all_args, ["w", "arg__3"]),
                                     lambda arg: arg > 0)
})
@Contract.post_conditions({
    "2nd Return value should be positive": lambda ret: ret[1] > 0
})
def untestable_function(x, y, z, w):
    return - (x * x + y * y), (z + w)


class TestUtilsDropArgs(unittest.TestCase):

    def test_successful_precondition_decorator_args(self):
        self.assertEqual(untestable_function(2, 3, 4, -3), (-13, 1))

    def test_successful_postcondition_decorator_args(self):
        self.assertEqual(untestable_function(2, 3, 4, -3), (-13, 1))

    def test_successful_precondition_decorator_kwargs(self):
        self.assertEqual(untestable_function(x=2, y=3, z=4, w=-3), (-13, 1))

    def test_successful_postcondition_decorator_kwargs(self):
        self.assertEqual(untestable_function(x=2, y=3, z=4, w=-3), (-13, 1))

    def test_successful_precondition_decorator_mixed(self):
        self.assertEqual(untestable_function(2, 3, z=4, w=-3), (-13, 1))

    def test_successful_postcondition_decorator_mixed(self):
        self.assertEqual(untestable_function(2, 3, z=4, w=-3), (-13, 1))
