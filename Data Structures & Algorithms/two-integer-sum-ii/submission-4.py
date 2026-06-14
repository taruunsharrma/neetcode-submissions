class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Array is sorted
        # We can use two pointers
        # one at the start, one at the end
        # if the i + j > target then we reduce j
        # if the i + j < target then we increase i

        i = 0
        j = len(numbers) - 1

        while i < j:

            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j]> target:
                # reduce the j
                j -= 1
                continue
            elif numbers[i]+ numbers[j] < target:
                # increase the i
                i += 1
                continue
        


