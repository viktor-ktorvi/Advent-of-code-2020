def find_next_operator(expression, operators):
    operator_locations = []
    for operator in operators:
        if expression.find(operator) != -1:
            operator_locations.append(expression.find(operator))

    if not operator_locations:
        return -1
    else:
        return min(operator_locations)


def operators_remaining(expression, operators):
    for operator in operators:
        if expression.find(operator) != -1:
            return True

    return False


def reduce_simple_expression(expression, operators):
    while operators_remaining(expression, operators):
        operator_location = find_next_operator(expression, operators)

        left_argument = expression[:operator_location]

        next_operator_location = operator_location + 1 + find_next_operator(expression[operator_location + 1:],
                                                                            operators)

        if next_operator_location == operator_location:
            right_argument = expression[operator_location + 1:]
        else:
            right_argument = expression[operator_location + 1:next_operator_location]

        result = ''
        if expression[operator_location] == '+':
            result = float(left_argument) + float(right_argument)
        elif expression[operator_location] == '*':
            result = float(left_argument) * float(right_argument)

        if next_operator_location == operator_location:
            expression = str(result)
        else:
            expression = str(result) + expression[next_operator_location:]

    return expression


def reduce_parentheses(expression, operators):
    while expression.find('(') != -1:
        left_parentheses = []
        right_parenthesis = []
        for i in range(len(expression)):
            if expression[i] == '(':
                left_parentheses.append(i)
            elif expression[i] == ')':
                right_parenthesis.append(i)

        j = 0
        while right_parenthesis[j] < left_parentheses[-1]:
            j += 1

        expression = expression[:left_parentheses[-1]] + \
                     reduce_simple_expression(expression[left_parentheses[-1] + 1:right_parenthesis[j]], operators) + \
                     expression[right_parenthesis[j] + 1:]

    return expression


def reduce_expression(expression, operators):
    return reduce_simple_expression(reduce_parentheses(expression, operators), operators)


if __name__ == '__main__':
    f = open('my_expressions.txt')
    expressions = f.read().split('\n')
    f.close()

    expressions = [expression.replace(" ", "") for expression in expressions]

    operators = ['+', '*']

    results = [float(reduce_expression(expression, operators)) for expression in expressions]

    print('Sum of results = {:.1f}'.format(sum(results)))
