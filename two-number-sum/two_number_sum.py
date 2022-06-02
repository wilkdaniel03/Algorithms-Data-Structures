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
