class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Brute force thinking
        # Loop over the array and get the counter
        # we need to sort the counter hash in desc form and retun the k most frequent number

        frequency = {}
        final_list = []

        for num in nums:
            if num in frequency:
                frequency[num]+= 1    
            else:
                frequency[num] = 1
        

        sorted_dict = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
        sorted_keys = list(sorted_dict.keys())

        return sorted_keys[:k]

