
class NotInMutableTagsException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.detail = msg
