class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Brute force thinking
        # Loop thru each string, sort it and store it

        collection = {}

        for each_string in strs:

            sorted_string = ''.join(sorted(each_string))
            if sorted_string in collection:
                collection[sorted_string].append(each_string)
            else:
                collection[sorted_string] = [each_string]

        return (list(collection.values()))