class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if len(s) != len(t):
        #     return False

        # # O(n) solution
        # return Counter(s) == Counter(t)


        if len(s)!= len(t):
            return False
        
        count_s = {}
        count_t = {}


        for each_char in s:
            if each_char in count_s:
                count_s[each_char]+=1
            else:
                count_s[each_char] = 1
        

        for each_char in t:
            if each_char in count_t:
                count_t[each_char]+=1
            else:
                count_t[each_char] = 1
    
        # Compare both strings 
        for each_char, value in count_s.items():
            if each_char not in count_t:
                return False
            else:
                if count_t[each_char] != value:
                    return False

        return True