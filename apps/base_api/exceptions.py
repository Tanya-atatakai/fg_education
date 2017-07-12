class JsonValidatorException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.detail = msg


class NotStrValue(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.detail = msg
