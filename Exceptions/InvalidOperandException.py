class InvalidOperandException(Exception):
    """Exception raised for invalid syntax(factorial must come after a number)"""

    def __init__(self, message):
        self.message = message
        super().__init__(message)