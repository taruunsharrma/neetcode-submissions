class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        unique_list = set(nums)
        res = 0
        for each_num in nums:
            streak = 0
            curr = each_num
            while curr in unique_list:
                streak += 1
                curr += 1
            res = max(res, streak)
        
        return res