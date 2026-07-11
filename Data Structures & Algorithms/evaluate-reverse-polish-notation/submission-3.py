class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for token in tokens:
            if token in operators:
                if token == '+':
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                        
                    stack.append(operand2 + operand1)

                elif token == '-':
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                        
                    stack.append(operand2 - operand1)

                elif token == '*':
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                        
                    stack.append(operand2 * operand1)

                elif token == '/':
                    operand1 = stack.pop()
                    operand2 = stack.pop()
                        
                    stack.append(int(operand2 / operand1))
            else:
                stack.append(int(token))
            
            print("stack:", stack)

        return stack[0]
            