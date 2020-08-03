from converters.primitives.int_converter import IntConverter, FloatConverter, BoolConverter


def can_convert_float(value):
    try:
        float(value)
        return True
    except:
        return False


def can_convert_int(value):
    try:
        int(value)
        return True
    except:
        return False


def can_convert_bool(value):
    return value in ['true', 'false', 'True', 'False']

class PrimitivesConverterFactory:
    def get_converter(self, value):
        if can_convert_int(value):
            return IntConverter()
        elif can_convert_float(value):
            return FloatConverter()
        elif can_convert_bool(value):
            return BoolConverter()

        raise TypeError(f'Converter not supported for {value}')
