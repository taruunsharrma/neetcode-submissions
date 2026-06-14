class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newStr = "".join(c.lower() for c in s if c.isalnum())
        
        if newStr == newStr[::-1]:
            return True
        return False