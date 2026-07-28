import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    
    # We Can also reverse in heap, using tuples
    # basically default heap is min heap
    # in python for tuple it will take first element 
    # so we will store the abs value which is without negative val

    heap = []

    for each_num in nums:
        pair = (-each_num, each_num)
        heapq.heappush(heap, pair)
        # this will store in min priority based on first element
    
    return [heapq.heappop(heap)[1] for i in range(len(heap))]



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
