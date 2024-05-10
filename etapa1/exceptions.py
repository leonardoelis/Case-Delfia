class InvalidFileStructureError(Exception):
    def __init__(self, message):
        self.message = message


class NonNumericValueError(Exception):
    def __init__(self, message):
        self.message = message
