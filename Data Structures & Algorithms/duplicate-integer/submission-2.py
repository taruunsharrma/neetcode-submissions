class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Hash Map Technique
        hash_map = set()

        for each_num in nums:

            if each_num in hash_map:
                return True
            
            hash_map.add(each_num)
        
        return False


