class SingletonInstance:
    _instance = None

    @classmethod
    def _getInstance(cls):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kwargs):
        cls._instance = cls(*args, **kwargs)
        cls.instance = cls._getInstance
        return cls._instance