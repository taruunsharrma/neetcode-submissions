class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        [2, 4, 5, 3, 1, 2]
        [5, 5, 3, 2, 2, -1]

        output = []
        for index, num in enumerate(arr, start=0):
            # We will hold a curr max
            max_number = -1
            for j in range(index+1, len(arr)):
                print(arr[j])
                if arr[j] > max_number:
                    max_number = arr[j]
            
            output.append(max_number)
        
        # output.append(-1)
        return output
