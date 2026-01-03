class InvalidInputException(Exception):
    """Exception raised for invalid input"""

    def __init__(self, message):
        self.message = message
        super().__init__(message)