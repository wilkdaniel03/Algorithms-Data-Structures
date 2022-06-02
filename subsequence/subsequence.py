class Subsequence:
    def run_approach_one(self, sequence, subsequence):
        sequence_idx = 0
        subsequence_idx = 0
        while sequence_idx < len(sequence) and subsequence_idx < len(subsequence):
            if sequence[sequence_idx] == subsequence[subsequence_idx]:
                subsequence_idx += 1
            sequence_idx += 1
        return subsequence_idx == len(subsequence)

    def run_approach_two(self, sequence, subsequence):
        subsequence_idx = 0
        for sequence_val in sequence:
            if sequence_val == subsequence[subsequence_idx]:
                subsequence_idx += 1
            if subsequence_idx == len(subsequence):
                break
        return subsequence_idx == len(subsequence)
