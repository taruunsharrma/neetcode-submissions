class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        # We need to get the count of each character from s and t
        s_count = {}
        t_count = {}

        unique_s = set(s)
        unique_t = set(t)

        for each_char in unique_s:
            count = s.count(each_char)
            s_count[each_char] = count
        
        for each_char in unique_t:
            count = t.count(each_char)
            t_count[each_char] = count
        
        for s_char, count in s_count.items():
            if s_char not in t_count:
                return False
            
            if t_count[s_char] != count:
                return False
        
        return True


