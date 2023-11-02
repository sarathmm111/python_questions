def evaluate(exp):
    stack = []
    for i in exp:
        if i in ['+','-','*','/','%']:
        
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            if i == "+":
                stack.append(operand_1 + operand_2)
            elif i == "-":
                stack.append( operand_1 - operand_2)
            elif i == "*":
                stack.append(operand_1 * operand_2)
            elif i == "/":
                stack.append(operand_1 // operand_2)
            elif i == "%":
                stack.append(operand_1 % operand_2) 
            elif i == "^":
                stack.append(operand_1 ** operand_2)
        else:
            stack.append(int(i))
    return stack.pop()


        
