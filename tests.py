import unittest
from main import to_upper


class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "ASHOK BHATTA"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, "ASHOK BHATTA")


if __name__ == '__main__':
    unittest.main()