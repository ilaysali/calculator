class NumbersInARowException(Exception):
    """Exception raised for invalid syntax(sequence of numbers separated by spaces)"""

    def __init__(self, message):
        self.message = message
        super().__init__(message)