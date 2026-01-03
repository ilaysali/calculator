class MismatchedParenthesesException(Exception):
    """Exception raised for invalid syntax(Invalid parentheses not the same number of parentheses)"""

    def __init__(self, message):
        self.message = message
        super().__init__(message)