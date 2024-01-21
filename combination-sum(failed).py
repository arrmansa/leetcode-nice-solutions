import numpy as np
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        final_output = []

        # get into numpy
        candidates_arr = np.array(candidates)

        # max repeats for each index + 0
        sizes = np.floor_divide(target, candidates_arr, dtype=np.int32) + 1

        # To create the weights
        rep_multiplier = np.empty(sizes.shape, dtype=np.int32)
        rep_multiplier[0] = 1
        rep_multiplier[1:] = np.cumprod(sizes)[:-1]

        length = np.product(sizes)
        
        MAX_WEIGHT_SIZE = 3000000
        
        weights = np.empty((MAX_WEIGHT_SIZE, candidates_arr.shape[0]), dtype=np.int32)

        for chunk_start in range(0, length, MAX_WEIGHT_SIZE):
            chunk_end = min(chunk_start+MAX_WEIGHT_SIZE, length)
            # create the weights
            if chunk_end == length:
                weights = np.empty((chunk_end-chunk_start, candidates_arr.shape[0]), dtype=np.int32)
            weights[:] = np.arange(chunk_start, chunk_end, dtype=np.int32)[:,np.newaxis]
            np.floor_divide(weights, rep_multiplier, out=weights)
            np.remainder(weights, sizes, out=weights)
            good_index = np.sum(weights * candidates_arr, axis=1) == target
            multipliers = weights[good_index].tolist()
            for row in multipliers:
                rowlist = []
                for num, times in zip(candidates, row):
                    rowlist += [num] * times
                final_output.append(rowlist)
        return final_output
