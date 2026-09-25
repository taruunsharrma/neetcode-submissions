class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # return Counter(s) == Counter(t)

        # another way is to do it manually
        # get the counter of each character and compare with  t
        
        s_count = defaultdict(int)
        t_count = defaultdict(int)

        for each_s in s:
            s_count[each_s] += 1
        
        for each_t in t:
            t_count[each_t] += 1
        
        return s_count == t_count