class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        # Hash map for quick lookup of the difference
        # The idea is get the num and its difference
        # so target is 7
        # first ele is 3
        # diff = target - num (7-3)= 4 (if 4 in lookup then return)
        # second ele is 4
        # diff = target - num (7 -4) = 3 (if 3 in lookup then return)

        hash_map = {}

        for index, each_num in enumerate(nums):

            diff = target - each_num
            if diff in hash_map:
                return [hash_map[diff], index]
            
            hash_map[each_num] = index
        