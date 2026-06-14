class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # O(nklogk), o(n.k)
        hash_map = defaultdict(list)
        # for word in strs:
        #     key = tuple(sorted(word))
        #     hash_map[key].append(word)
        # return list(hash_map.values())

        # o(n.k), o(n.k) better
        # for word in strs:
        #     key = [0]*26
        #     for c in word:
        #         key[ord(c) - ord('a')] += 1
        #         print(key)
        #     return
        #     hash_map[tuple(key)].append(word)
        # return list(hash_map.values())
        

        # Solution by neetcode
        for each_word in strs:

            keys = [0]*26 # 26 alphabets 
            for each_char in each_word:
                keys[ord(each_char) - ord("a")] +=1
            
            hash_map[tuple(keys)].append(each_word)
        print(hash_map)
        return list(hash_map.values())