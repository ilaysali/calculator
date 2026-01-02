class TokenNotDefineException(Exception):
    """Exception raised for undefined token."""

    def __init__(self, message):
        self.message = message
        super().__init__(message)