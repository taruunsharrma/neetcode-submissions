class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        # return min(nums) # o (n)

        # if we need to reduce the time complexity and find the min num, we can use heap

        import heapq

        heapq.heapify(nums)

        return nums[0]