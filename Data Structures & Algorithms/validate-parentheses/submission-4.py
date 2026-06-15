class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        if len(s) < 2:
            return False

        for each_char in s:

            if each_char in ["(", "[", "{"]:
                stack.append(each_char)
                continue

            if each_char in [")", "]", "}"]:
                if stack:
                    top = stack.pop()
                    print(top)
                    if top == '(' and each_char == ')':
                        continue
                    elif top == '[' and each_char == ']':
                        continue
                    elif top == '{' and each_char == '}':
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                return False
        
        if stack:
            return False
        else:
            return True