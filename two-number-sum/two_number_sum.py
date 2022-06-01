class TwoNumberSum:
    def ensure_input_is_correct(self, array):
        if not array:
            return False
        else:
            return True

    def run_approach_one(self, array, expectedSum):
        if self.ensure_input_is_correct(array) == False:
            raise ValueError()
