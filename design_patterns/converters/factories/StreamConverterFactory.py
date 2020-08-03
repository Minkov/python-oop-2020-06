from converters.streams.CsvStreamConverter import CsvStreamConverter
from converters.streams.JsonStreamConverter import JsonStreamConverter

from converters.decorators.PrimitiveValuesDecoratorConverter import PrimitiveValuesDecoratorStreamConverter


class StreamConverterFactory:
    def __init__(self):
        self.converters = {
            'application/json': JsonStreamConverter(),
            'application/vnd.ms-excel': PrimitiveValuesDecoratorStreamConverter(CsvStreamConverter()),
        }

    def get_converter(self, type):
        if type not in self.converters:
            raise ValueError(f'No converter for type {type}')

        return self.converters[type]
