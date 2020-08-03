def singleton(cls):
    instance = [None]

    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return wrapper


@singleton
class DataImporter:
    def __init__(self):
        pass

    @classmethod
    def static_m(cls):
        print('I am static')


class Singleton:
    instances = {}

    def __new__(cls, *args, **kwargs):
        if cls.__name__ not in cls.instances:
            cls.instances[cls.__name__] = cls.__new__(cls, *args, **kwargs)
        return cls.instances[cls.__name__]

class DataImporter2(Singleton):
    pass


d1 = DataImporter2()
d2 = DataImporter2()