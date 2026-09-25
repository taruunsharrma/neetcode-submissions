class Solution:
    def isPalindrome(self, s: str) -> bool:
        # return s.lower() == s[::-1].lower()

        # lets use two pointers
        left = 0
        right = len(s) -1

        while left < right:
            if not s[left].lower().isalnum():
                # increase left
                left += 1
                continue
            
            if not s[right].lower().isalnum():
                # reduce right
                right -= 1
                continue

            # compare
            if s[left].lower()!= s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
