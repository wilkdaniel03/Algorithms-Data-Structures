import unittest
import sorted_squared_array as sqa

class TestSortedSquaredArray(unittest.TestCase):
    def test_basic_approach(self):
        my_sorted_squared_array = sqa.SortedSquaredArray()
        my_example_input_array = [1,2,3,4,5,15,25,100]
        print(my_sorted_squared_array.basic_approach(my_example_input_array))

    def test_complex_approach(self):
        my_sorted_squared_array = sqa.SortedSquaredArray()
        my_example_input_array = [-4,1,2,3,4,5]
        print(my_sorted_squared_array.complex_approach(my_example_input_array))

if __name__ == "__main__":
    unittest.main()
