class Solution:
    def twoSum(self, nums: List[int], target: int):
        
        # Brute force thinking
        # two iteration on the list to get the target o(n2)
        # another solution is find the difference in the list 0(n)
        # using two pointers technique

        diff_hash = {}

        for index, num in enumerate(nums):

            # get the difference
            difference = target - num
            if difference in diff_hash:
                return [diff_hash[difference], index]
            else:
                diff_hash[num] = index
    
        print(diff_hash)


            



