class ArcBaseException(BaseException):
    pass


class ArcInvaidUserCodeException(ArcBaseException):
    pass


class ArcUnknownException(ArcBaseException):
    def __init__(self, details: str):
        self.details = details

    def __str__(self):
        return f'<ArcUnknownException, error={self.details}>'

    def __repr__(self):
        return self.__str__()