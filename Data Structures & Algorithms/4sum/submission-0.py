class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # Intuition
        # We will start with two pointers
        # i, j, l, m
        # if i+j+l+m matches the target then store that in arr
        # if not increase j+l+m to get till target
        # Once we get the right arr then we will be 
        nums.sort()
        res = set()
        
        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                for c in range(b+1, len(nums)):
                    for d in range(c+1, len(nums)):
                        if nums[a]+nums[b]+nums[c]+nums[d] == target:
                            res.add((nums[a], nums[b], nums[c], nums[d]))

        return list(res) 