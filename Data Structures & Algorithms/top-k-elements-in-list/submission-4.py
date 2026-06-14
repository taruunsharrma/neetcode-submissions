import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # count = Counter(nums)
        # heap = []
        
        # for num, freq in count.items():
        #     heapq.heappush(heap, (freq, num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # print(heap)
        # return [num for freq, num in heap]



        counts = Counter(nums)
        # buckets = [[] for _ in range(len(nums))]
        buckets = [[] for _ in range(len(nums) + 1)]


        print(buckets)
        print(counts)

        # Add the count in the bucket
        # So for example, if count is Counter({3: 3, 2: 2, 1: 1})
        # Then we will add at 3rd index 3 will go
        # at 2nd index 2 will go and at 1st index 1 will go
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        #[[], [1], [], [2, 3], [], [], []]
        # Now from top k we need to return result
        result = []
        for each_bucket in buckets[::-1]:
            for each_num in each_bucket:
                result.append(each_num)
                if len(result) == k:
                    return result
        
        return result




