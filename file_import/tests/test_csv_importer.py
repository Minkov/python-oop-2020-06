from io import StringIO, BytesIO
from unittest import TestCase

from import_strategies.csv_importer import CsvImporter


class TestCsvImporter(TestCase):
    def setUp(self) -> None:
        self.importer = CsvImporter()

    def test_getData_whenDataIsValid_shouldReturnCorrectResult(self):
        csv = '''name, age
        Gosho, 13'''

        stream = StringIO(csv)
        expected = [
            ('name', 'Gosho',),
            ('age', '13')
        ]

        actual = self.importer.get_data_from_stream(stream)
        self.assertEqual(expected, actual)
