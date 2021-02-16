class AuthError(Exception):
    def __init__(
            self,
            message=None):
        super(AuthError, self).__init__(message)

        self._message = message

    def __str__(self):
        return self._message


class KeyError(AuthError):
    pass
