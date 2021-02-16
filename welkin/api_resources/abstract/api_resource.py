import welkin


class APIResource():
    @classmethod
    def class_url(cls):
        if cls == APIResource:
            raise NotImplementedError(
                "APIResource is an abstract class. You should perform"
                "actions on its subclass (e.g. Patient)"
            )
        api_base = welkin.api_base
        api_version = welkin.api_version
        object_name = cls.OBJECT_NAME
        base = api_base + '/' + api_version + '/' + object_name
        return base
