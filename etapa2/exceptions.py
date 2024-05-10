class CityNotFoundError(Exception):
    def __init__(self, message):
        self.message = message


class APIError(Exception):
    def __init__(self, message):
        self.message = message
