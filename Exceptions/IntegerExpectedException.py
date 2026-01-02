class IntegerExpectedException(Exception):
    """Exception raised for invalid syntax(factorial can only be used on integers)"""

    def __init__(self, message):
        self.message = message
        super().__init__(message)