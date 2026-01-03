# Omega Calculator

**Omega Calculator** is a mathematical expression evaluator built from scratch in Python. The project handles complex inputs and edge cases without relying on external mathematical libraries.

## Key Features
* **Input Handling:** Processes inputs with tabs and whitespaces.
* **Operator Reform:** reforms sequences of ('-', '+') via mathematical logic.
* **Advanced Parsing:** Implements the **Shunting-yard algorithm** to convert expressions to Postfix notation.
* **Custom Error Handling:** Specific feedback for syntax errors, missing operands, mismatched parentheses, and division by zero.
* **Pure Python:** Built entirely with standard libraries — no external dependencies.

## Project Structure
* `main.py`: Entry point and user interface loop.
* `reform.py`: Cleans whitespace and normalizes operator sequences.
* `Parser(shunting_yard.py, tokenizer.py)`: Tokenizes input and manages the parsing logic.
* `evaluate.py`: Calculates the result using postfix evaluation.
* `Exceptions`: Custom exception classes for precise error reporting.

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/ilaysali/calculator.git](https://github.com/ilaysali/calculator.git)
