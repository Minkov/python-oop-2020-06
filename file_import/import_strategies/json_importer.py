from json import loads

from import_strategies.base_importer import BaseImporter


class JsonImporter(BaseImporter):
    def get_data_from_stream(self, stream):
        stream.seek(0)
        json = stream.read(1 << 20)
        d = loads(json)
        return [(key, value) for (key, value) in d.items()]
