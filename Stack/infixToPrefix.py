def infix_to_prefix(expression):
    def precedence(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0

    def infix_to_postfix(expression):
        stack = []
        result = []
        for char in expression:
            if char.isalnum():
                result.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and precedence(stack[-1]) >= precedence(char):
                    result.append(stack.pop())
                stack.append(char)
        while stack:
            result.append(stack.pop())
        return ''.join(result)

    def reverse_expression(expression):
        expression = expression[::-1]
        expression = list(expression)
        for i in range(len(expression)):
            if expression[i] == '(':
                expression[i] = ')'
            elif expression[i] == ')':
                expression[i] = '('
        return ''.join(expression)

    reversed_expression = reverse_expression(expression)
    postfix_expression = infix_to_postfix(reversed_expression)
    prefix_expression = reverse_expression(postfix_expression)
    return prefix_expression

# Example usage:
expression = "(A-B/C)*(A/K-L)"
print("Infix: ", expression)
print("Prefix: ", infix_to_prefix(expression))