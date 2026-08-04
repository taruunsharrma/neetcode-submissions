class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        

        # Find the matching subsequent character from t with s
        # Remaining characters of t will be the answer
        # Use two pointers
        # s = 'abcde' t = 'happy'
        # hppy



        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        
        return len(t) -j 