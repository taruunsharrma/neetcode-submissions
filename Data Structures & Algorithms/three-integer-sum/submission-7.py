class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # res = []

        # for i in range(len(nums)-2):

        #     # Skip duplicate first elements
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
            
        #     # create pointers
        #     left = i + 1
        #     right = len(nums) - 1

        #     while left < right:
        #         total = nums[i] + nums[left] + nums[right]
                
        #         if total < 0:
        #             left += 1

        #         elif total > 0:
        #             right -= 1
                
        #         else:
        #             res.append([nums[i], nums[left], nums[right]])
            
        #             left += 1
        #             right -= 1

        #             # Skip duplicates
        #             while left < right and nums[left] == nums[left - 1]:
        #                 left += 1

        #             while left < right and nums[right] == nums[right + 1]:
        #                 right -= 1

        # return res



        # Let's try brute force solution
        # Time Limit Exceeded for this solution
        # res = set()
        # nums.sort()

        # for a in range(len(nums)):
        #     for b in range(a+1, len(nums)):
        #         for c in range(b+1, len(nums)):
        #             if nums[a] + nums[b] + nums[c] == 0:
        #                 res.add((nums[a], nums[b], nums[c]))

        # return list(res)

        # Using Two pointers technique
        # The way we solved 2sum where diff = target - num  and then lookup on hash for the diff
        # Similar way we need to solve 3 sum
        # Here we will first sort the array
        # Sorting will help us because we can get the right answer faster using two pointers,
        # The pointer logic will only work once we understand whether our diff is large or small
        # Based on that we will move our pointer or else it without pointer we will have to try all combinations

        res = set()
        nums.sort()

        for i in range(len(nums)-1):
            # First element is the starting point
            _num = nums[i]
            # Now we will create two pointers left and right and once we find the right combiation
            # left+right+_num=0 we add to the set
            left = i+1
            right = len(nums)-1
            while left < right:
                # Check whether we are meeting the target or not
          
                if _num + nums[left] + nums[right] == 0:
                    res.add((_num, nums[left], nums[right]))
                    left += 1
                    right -= 1

                elif _num + nums[left] + nums[right] > 0: # If it is greater than 0, that means we need to reduce from right side, so we can get less value
                    right -= 1
                elif _num + nums[left] + nums[right] < 0:
                    # It means the number is coming big so we need to increase left sied
                    left += 1
                else:
                    continue
            
        return list(res)
                


