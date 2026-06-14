class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # brute force
        # keep track of the number in a hash and return true if its seen agian
        # 0(1)

        num_seen = {}

        for num in nums:

            if num in num_seen:
                return True
            
            num_seen[num] = True
        
        return False
