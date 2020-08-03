from import_strategies.base_importer import BaseImporter
from utils.utils import flip_matrix


class CsvImporter(BaseImporter):
    def get_data_from_stream(self, stream):
        def decode(text):
            try:
                return text.decode()
            except:
                pass
            return text

        stream.seek(0)
        rows = [[c.strip().strip()
                 for c in decode(row).strip().split(',')]
                for row in stream.readlines()]

        return flip_matrix(rows)
