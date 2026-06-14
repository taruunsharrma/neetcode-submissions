class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Intuitive approach
        # Sort the array and find the index where the sequence ends
        
        # Another approach
        # Loop thru the array, and for each loop check the consequetive numbers
        # O{N2} approach

        final_output = []

        for index, number in enumerate(nums, start=0):
            # Check whether we have a consequtive numbers from this number
            # if yes then add this in the list
            consequtive = [number]
            next_number = number + 1
            while next_number in nums:
                consequtive.append(next_number)
                next_number += 1
            
            if len(consequtive) > len(final_output):
                final_output = consequtive
            
        
        return len(final_output)






