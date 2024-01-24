# Propositional Logic Argument Evaluator

## Overview
This project implements a simple propositional logic argument evaluator. It takes premises and a conclusion expressed in natural language and evaluates whether the argument is valid using propositional logic.

## Components

### 1. Logic Function
The `logic` function converts logical connectives in the natural language input to symbolic notation. It replaces words like 'and', 'or', 'not', 'if', 'then', 'iff', etc., with their corresponding symbols.

### 2. Evaluate Argument Function
The `evaluate_argument` function takes premises and a conclusion, generates truth value combinations for variables, and evaluates the validity of the argument using propositional logic.

### 3. Generate Combinations Function
The `generate_combinations` function creates all possible truth value combinations for a given set of variables.

### 4. Evaluate Expression Function
The `evaluate_expression` function evaluates a logical expression using truth values for variables and logical connectives.

## Usage
1. **Install Python:**
   - Ensure you have Python installed on your system.

2. **Run the Evaluator:**
   - Execute the provided code in a Python environment.
   - Modify the `english_premises` and `english_conclusion` variables with your logical argument.

3. **Review Output:**
   - The program will output whether the argument is valid or not based on the evaluation.

## Example
```python
english_premises = [
    "If today is Tuesday, then I have a test in English or Science.",
    "If my English Professor is absent, then I will not have a test in English.",
    "Today is Tuesday.",
    "My English Professor is absent."
]
english_conclusion = "I have a test in Science."

# The argument is not valid.
```
## License
This project is licensed under the MIT License.

Feel free to use, modify, and distribute. Contributions are welcome!

Happy logical reasoning!
