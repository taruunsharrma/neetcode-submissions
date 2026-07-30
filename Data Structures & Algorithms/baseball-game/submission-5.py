class Solution:
    def calPoints(self, operations: List[str]) -> int:
        

        stack = []


        # append
        # pop
        
        for op in operations:
            if op == '+':
                # We need to sum the previous two scores
                first = int(stack[-1])
                second = int(stack[-2])
                third = first + second
                stack.append(third)
                print(str(op), stack)
            elif op == 'C':
                # We need to invalidate the previous score
                stack.pop()
                print(str(op), stack)
            elif op == 'D':
                # WE need to doube the score and add it
                first = int(stack[-1])
                double = 2 * first
                stack.append(double)
                print(str(op), stack)
            else:
                stack.append(int(op))
                print(str(op), stack)

        
        # print(stack)
        return sum(stack)