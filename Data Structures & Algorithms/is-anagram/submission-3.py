class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Get each character count
        # compare whether the count matches or not

        if len(s) != len(t):
            return False

        char_count_s = {}
        char_count_t = {}

        for each_char in s:
            if each_char in char_count_s:
                char_count_s[each_char] += 1
            else:
                char_count_s[each_char] = 1
        
        for each_char in t:
            if each_char in char_count_t:
                char_count_t[each_char] += 1
            else:
                char_count_t[each_char] = 1
        
        for char_name, count in char_count_s.items():
            if char_name not in char_count_t:
                return False
            
            t_count = char_count_t[char_name]
            if count != t_count:
                return False
        
        return True