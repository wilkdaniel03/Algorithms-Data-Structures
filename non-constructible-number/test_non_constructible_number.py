import unittest
import non_constructible_number as ncn

class TestNonConstructibleNumber(unittest.TestCase):
    def test_run_algorithm(self):
        my_ncn = ncn.NonConstructibleNumber()
        print(my_ncn.run([2,2,5]))

if __name__ == "__main__":
    unittest.main()
