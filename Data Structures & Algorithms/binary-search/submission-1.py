class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def recursion(left, right):

            if left > right:
                return -1

            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            elif nums[middle] < target:
                return recursion(middle + 1, right)

            else:
                return recursion(left, middle - 1)

        return recursion(0, len(nums) - 1)