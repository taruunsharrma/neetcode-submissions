class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(k):
            last_ele = nums[-1]
            nums.pop()
            nums.insert(0, last_ele)
        return nums