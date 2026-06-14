class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Dict to store the difference
        final_tally = {}

        for index, each_num in enumerate(nums, start=0):
            diff = target - each_num

            if diff in final_tally:
                return [final_tally[diff], index]
            final_tally[each_num] = index
        return