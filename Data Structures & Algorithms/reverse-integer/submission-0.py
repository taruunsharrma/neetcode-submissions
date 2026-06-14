class Solution:
    def reverse(self, x: int) -> int:
        INT32_MIN = -2**31
        INT32_MAX = 2**31 - 1

        string = str(x)
        if string[0] == '-':
            update_string = string[1:]
            reverse_string = '-' + update_string[::-1]
        else:
            reverse_string = string[::-1]
        
        numeric = int(reverse_string)

        if numeric > INT32_MIN and numeric < INT32_MAX:
            return numeric
        else:
            return 0