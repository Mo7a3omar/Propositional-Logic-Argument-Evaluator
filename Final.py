def logic(proposition):
    operators = {
        'and': '&', 'or': '|', 'not': '~', 'if': '->', 'then': '->', 'iff': '<->',
        'if and only if': '<->', 'implies': '->',
        'is equivalent to': '<->', 'equals': '<->'
    }
    for word, symbol in operators.items():
        proposition = proposition.replace(word, symbol)

    proposition = proposition.replace('(', '( ')
    proposition = proposition.replace(')', ' )')
    return proposition


def evaluate_argument(premises, conclusion):
    variables = set()
    for premise in premises:
        variables.update(set(premise.split()))
    variables.update(set(conclusion.split()))

    combinations = generate_combinations(list(variables))

    for combination in combinations:
        truth_values = dict(zip(variables, combination))
        valid = evaluate_expression(premises, conclusion, truth_values)
        if valid:
            return True

    return False


def generate_combinations(variables):
    num_variables = len(variables)
    num_combinations = 2 ** num_variables

    combinations = []
    for i in range(num_combinations):
        combination = []
        for j in range(num_variables):
            combination.append((i // (2 ** j)) % 2)
        combinations.append(combination[::-1])

    return combinations


def evaluate_expression(premises, conclusion, truth_values):
    operators = {
        '&': lambda x, y: x and y,
        '|': lambda x, y: x or y,
        '~': lambda x: not x,
        '->': lambda x, y: (not x) or y
    }

    for premise in premises:
        tokens = premise.split()
        stack = []

        for token in tokens:
            if token in operators:
                if token == '~':
                    operand = stack.pop()
                    result = operators[token](operand)
                else:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    result = operators[token](operand1, operand2)
                stack.append(result)
            else:
                stack.append(truth_values[token])

        if not stack[0]:
            return False

    conclusion_tokens = conclusion.split()
    conclusion_stack = []

    for token in conclusion_tokens:
        if token in operators:
            if token == '~':
                operand = conclusion_stack.pop()
                result = operators[token](operand)
            else:
                operand2 = conclusion_stack.pop()
                operand1 = conclusion_stack.pop()
                result = operators[token](operand1, operand2)
            conclusion_stack.append(result)
        else:
            conclusion_stack.append(truth_values[token])

    return conclusion_stack[0]

english_premises = [
    "If today is Tuesday, then I have a test in English or Science.",
    "If my English Professor is absent, then I will not have a test in English.",
    "Today is Tuesday.",
    "My English Professor is absent."
]
english_conclusion = "I have a test in Science."

premises = [logic(premise) for premise in english_premises]
conclusion = logic(english_conclusion)

result = evaluate_argument(premises, conclusion)

if result:
    print("The argument is valid.")
else:
    print("The argument is not valid.")
