class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        # return min(nums) # o (n)

        # if we need to reduce the time complexity and find the min num, we can use heap

        # import heapq

        # heapq.heapify(nums)

        # return nums[0]

        # lets use binary search to run in o(log n ) time


        # for binary search we keep running the loop
        

        # left = 0
        # right = len(nums) - 1

        # while left < right:
        #     mid = left + (right - left) // 2
        #     # mid = 0 + (5 - 0)//2 = 4
        #     # mid = 2 + (5-2)//2 = 3

        #     if nums[mid] > nums[right]:
        #         left = mid + 1
        #     else:
        #         right = mid

        # return nums[left]

        # lets rewrite the logic

        left = 0
        right = len(nums) - 1

        while left < right:
            # find the middle
            mid = left + (right - left)//2

            # now check if the target( which is the min number) is greater or less than mid
            if nums[mid] > nums[right]:
                # now in this case, we now know that the target is to the right
                # so we now update our left pointer to the mid and repeat again
                left = mid+1
            else:
                # here if the mid number is less than right, which means answer lies to the left
                # so we update our end right to the mid
                right = mid
            
        
        return nums[left]


        