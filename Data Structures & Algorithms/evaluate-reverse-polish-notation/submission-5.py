class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token in operators:
                operand1 = stack.pop()
                operand2 = stack.pop()

                if token == '+':    
                    stack.append(operand2 + operand1)

                elif token == '-':
                    stack.append(operand2 - operand1)

                elif token == '*':
                    stack.append(operand2 * operand1)

                elif token == '/':
                    stack.append(int(operand2 / operand1))
            else:
                stack.append(int(token))

        return stack[0]
            