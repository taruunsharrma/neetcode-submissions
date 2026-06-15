class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # unique_list = set(nums)
        # res = 0
        # for each_num in nums:
        #     streak = 0
        #     curr = each_num
        #     while curr in unique_list:
        #         streak += 1
        #         curr += 1
        #     res = max(res, streak)
        
        # return res


        # Optimal using hashmap
        # mp = defaultdict(int)
        # res = 0

        # for num in nums:
        #     if not mp[num]:
        #         mp[num] = mp[num - 1] + mp[num + 1] + 1
        #         mp[num - mp[num - 1]] = mp[num]
        #         mp[num + mp[num + 1]] = mp[num]
        #         res = max(res, mp[num])
        # return res


        #  This solution is ideally 0(n) but for 1,2,3,4,5 arr it will check all ele which will give us 0(n2)
        # To solve that and bring it to O(n) we need to check whether the curr number is at the start of the sequence or not
        unique_lst = set(nums)
        streak = 0

        for each_num in nums:
            res = 0
            curr_num = each_num

            if curr_num - 1 not in unique_lst:

                num = curr_num

                while num in unique_lst:
                    res += 1
                    num += 1
                
                streak = max(res, streak)

        return streak

            




























