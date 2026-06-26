class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        # Idea is whenever we will get the operator
        # We will pop the operand and perform operation
        # then update the stack
        operators = ["+", "-", "*", "/"]

        for each_token in tokens:

            # Identify whether the token is Operator or Operand
            if each_token not in operators:
                stack.append(int(each_token))
                continue
            
            # pop the operands
            op1 = stack.pop()
            op2 = stack.pop()

            if each_token == "+":
                stack.append(op2 + op1)

            elif each_token == "-":
                stack.append(op2 - op1)

            elif each_token == "*":
                stack.append(op2 * op1)

            else:
                # LeetCode wants division truncated toward zero
                stack.append(int(op2 / op1))
                    
        return stack.pop()
