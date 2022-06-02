class SortedSquaredArray:
    def basic_approach(self, array):
        squared_array = [0 for _ in array]
        idx = 0
        for x in array:
            squared_array[idx] = x*x
            idx += 1
        squared_array.sort()
        return squared_array

    def complex_approach(self, array):
        squared_array = [0 for _ in array]
        smallest_number_idx = 0
        largest_number_idx = len(array)-1
        for idx in reversed(range(0, len(array))):
            smallest_value = array[smallest_number_idx]
            largest_value = array[largest_number_idx]
            if abs(smallest_value) > abs(largest_value):
                squared_array[idx] = smallest_value ** 2
                smallest_number_idx += 1
            else:
                squared_array[idx] = largest_value ** 2
                largest_number_idx -= 1
        return squared_array
