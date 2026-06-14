from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # using division Operation
        # get the product of entire list
        # and loop through each num and divide the final prod, this can give you right answer
        # Except the final prod is 0, then we can get zero division error

        # Hence we wil use another method
        # prefix and postfix concept,
        # arr = [1, 2, 3, 4]
        # prefix = [1, 1, 2, 6]
        # postfix = [24, 12, 4, 1]
        # prod = [24, 12, 8, 6]


        prod = []
        prefix_list = [1]*len(nums)
        postfix_list = [1]*len(nums)

        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            prefix_list[i] = prefix
            prefix *= nums[i]
        
        for j in range(len(nums)-1, -1, -1):
            postfix_list[j] = postfix
            postfix *= nums[j]
        
        final = []
        for v1, v2 in zip(prefix_list, postfix_list):
            final.append(v1*v2)
        
        return final





        # n = len(nums)
        # ans = [1] * n

        # prefix = 1
        # for i in range(n):
        #     ans[i] = prefix
        #     prefix *= nums[i]

        # postfix = 1
        # for i in range(n - 1, -1, -1):
        #     ans[i] *= postfix
        #     postfix *= nums[i]

        # return ans