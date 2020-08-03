from import_strategies.base_importer import BaseImporter


def should_convert(value):
    return type(value) != str


def convert_to_integer_or_default(value):
    if should_convert(value):
        return value
    try:
        return int(value)
    except:
        return value


def convert_to_float_or_default(value):
    if should_convert(value):
        return value
    try:
        return float(value)
    except:
        return value


def convert_to_bool_or_default(value):
    if value not in ['true', 'false']:
        return value
    return value == 'true'


class PrimitiveValuesImporterDecorator(BaseImporter):
    def __init__(self, importer: BaseImporter):
        self.importer = importer

    def get_data_from_stream(self, stream):
        data = self.importer.get_data_from_stream(stream)

        data = self.__fix(data, convert_to_integer_or_default)
        data = self.__fix(data, convert_to_float_or_default)
        data = self.__fix(data, convert_to_bool_or_default)

        return data

    def __fix(self, data, func):
        return [[func(value)
                 for value in row]
                for row in data]
