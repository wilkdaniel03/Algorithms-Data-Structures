class TwoNumberSum:
    def ensure_input_is_correct(self, array):
        if not array:
            return False
        else:
            return True

    def run_approach_one(self, array, expectedSum):
        if self.ensure_input_is_correct(array) == False:
            raise ValueError("Input array cannot be empty")
        for x in range(0, len(array) -1):
            for y in range(x+1, len(array)):
                if x+y == expectedSum:
                    return [x,y]
        return []

    def run_approach_two(self, array, expectedSum):
        if self.ensure_input_is_correct(array) == False:
            raise ValueError("Input array cannot be empty")
        nums = {}
        for x in array:
            num = expectedSum - x
            if num in nums:
                return [x,num]
            else:
                nums[x] = True
        return []

    def run_approach_three(self, array, expectedSum):
        if self.ensure_input_is_correct(array) == False:
            raise ValueError("Input array cannot be empty")
        array.sort()
        left = 0
        right = len(array)-1
        while right<len(array)-1 and left<right:
            result = array[left]+array[right]
            if result == expectedSum:
                return [array[left],array[right]]
            elif result<expectedSum:
                left += 1
            elif result>expectedSum:
                right -= 1
        return []
