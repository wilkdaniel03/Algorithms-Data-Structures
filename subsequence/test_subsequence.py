import unittest
import subsequence as sq

class TestSequence(unittest.TestCase):
    def test_approach_one(self):
        my_sequence = sq.Subsequence() 
        my_example_sequence = [1,2,3,4,5,6,7,8,9]
        my_example_subsequence = [2,4,6,8]
        result = my_sequence.run_approach_one(my_example_sequence, my_example_subsequence)
        self.assertEqual(True, result)

    def test_approach_two(self):
        my_sequence = sq.Subsequence() 
        my_example_sequence = [1,2,3,4,5,6,7,8,9]
        my_example_subsequence = [2,4,6,8]
        result = my_sequence.run_approach_one(my_example_sequence, my_example_subsequence)
        self.assertEqual(True, result)

if __name__ == "__main__":
    unittest.main()
