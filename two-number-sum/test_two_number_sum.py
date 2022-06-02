import unittest
import two_number_sum

class TestTwoNumberSum(unittest.TestCase):
    def test_input_empty_array_approach_one(self):
        my_two_number_sum = two_number_sum.TwoNumberSum()
        with self.assertRaises(ValueError):
            my_two_number_sum.run_approach_one([], 10)

    def test_input_empty_array_approach_two(self):
        pass

    def test_input_empty_array_approach_three(self):
        pass

    def test_result_approach_one(self):
        my_two_number_sum = two_number_sum.TwoNumberSum()
        self.assertEqual([1,4], my_two_number_sum.run_approach_one([1,2,3,4,5], 5))

    def test_result_approach_two(self):
        pass

    def test_result_approach_three(self):
        pass

if __name__ == "__main__":
    unittest.main()
