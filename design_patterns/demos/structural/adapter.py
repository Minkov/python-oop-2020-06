from abc import ABC, abstractmethod
from csv import reader
from io import StringIO
from json import loads


class BaseConverter(ABC):
    @abstractmethod
    def convert(self, data):
        pass


class JsonConverter(BaseConverter):
    def convert(self, data):
        return loads(data)


class CsvConverter(BaseConverter):
    def convert(self, data):
        csv = reader(StringIO(data))
        lines = [line for line in csv]
        return lines


def convert(type, data):
    converters = {
        'json': JsonConverter(),
        'csv': CsvConverter(),
    }

    return converters[type] \
        .convert(data)
