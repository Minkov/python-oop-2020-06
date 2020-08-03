from abc import ABC, abstractmethod
from json import loads


class DataConverter(ABC):
    @abstractmethod
    def to_dict(self, data):
        pass


class JsonDataConverter(DataConverter):
    def to_dict(self, data):
        return loads(data)


class CsvDataConverter(DataConverter):
    def to_dict(self, data):
        return None


class DataConverterAbstractFactory(ABC):
    @abstractmethod
    def get_json_converter(self):
        pass

    @abstractmethod
    def get_csv_converter(self):
        pass


class DataConverterFactory(ABC):
    @abstractmethod
    def get_converter(self, type) -> DataConverter:
        pass


class JsonDataConverterFactory(DataConverterFactory):
    def get_converter(self, type=None) -> DataConverter:
        return JsonDataConverter()


class ConcreteDataConverterFactory(DataConverterFactory):
    def get_converter(self, type) -> DataConverter:
        if type == 'json':
            return JsonDataConverter()
        elif type == 'csv':
            return CsvDataConverter()

        raise ValueError('Invalid converter type!')


csv = """
name, age
Doncho, 19
"""

json = '''
{
    "name": "Doncho",
    "age": 18
}
'''


def convert(type, data):
    factory = ConcreteDataConverterFactory()
    return factory.get_converter(type) \
        .to_dict(data)


converter = JsonDataConverter()
result = converter.to_dict(json)
print(result)
print(result.items())
