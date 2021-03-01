class BaseException(Exception):
    def __init__(self, message:str=None):
        self.message = message
    
    def _message(self):
        return self.message

class NotFound(BaseException):
    pass
