class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hash_map = {}

        for index, each_num in enumerate(nums):

            if each_num in hash_map:
                return True
            
            hash_map[each_num] = index
        
        return False