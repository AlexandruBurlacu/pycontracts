import unittest
from pycontracts import utils

class TestUtils(unittest.TestCase):
    
    def setUp(self):
        self.dictionary = {
            "arg__0": 12,
            "arg__1": 32,
            "some_other_argument": 128
            }

    def test_check_any(self):
        self.assertEqual(utils.check_any(self.dictionary, lambda arg: arg is list), False)

    def test_check_all(self):
        self.assertEqual(utils.check_all(self.dictionary, lambda arg: arg > 0), True)

    def test_drop_fst_arg(self):
        self.assertDictEqual(utils.drop_fst_arg(self.dictionary),
                             {"arg__1": 32, "some_other_argument": 128})

    def test_drop_args(self):
        self.assertDictEqual(utils.drop_args(self.dictionary, ["some_other_argument", "arg__3"]),
                             {"arg__0": 12, "arg__1": 32})

    def tearDown(self):
        self.dictionary.clear()

