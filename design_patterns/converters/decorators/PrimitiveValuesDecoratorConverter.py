from converters.factories.PrimitivesConverterFactory import PrimitivesConverterFactory
from converters.streams.StreamConverter import StreamConverter

primitives_converter_factory = PrimitivesConverterFactory()


class PrimitiveValuesDecoratorStreamConverter(StreamConverter):
    def __init__(self, converter: StreamConverter):
        self.converter = converter

    def convert_from_stream(self, stream):
        result = self.converter.convert_from_stream(stream)

        for (key, value) in result.items():
            try:
                converter = primitives_converter_factory.get_converter(value)
                result[key] = converter.convert(value)
            except:
                pass

        return result
