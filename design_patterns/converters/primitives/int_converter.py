class IntConverter:
    def convert(self, str):
        return int(str)

class FloatConverter:
    def convert(self, str):
        return float(str)

class BoolConverter:
    def convert(self, str):
        return str in ['True', 'true']