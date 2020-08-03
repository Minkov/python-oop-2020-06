from io import StringIO
from unittest import TestCase

from import_strategies.json_importer import JsonImporter


class TestJsonImporter(TestCase):
    def setUp(self) -> None:
        self.importer = JsonImporter()

    def test_getData_whenDataIsValid_shouldReturnCorrectResult(self):
        json = '''
        {
            "name": "Gosho",
            "age": 13
        }
'''

        stream = StringIO(json)
        expected = [
            ('name', 'Gosho',),
            ('age', 13)
        ]

        actual = self.importer.get_data_from_stream(stream)
        self.assertEqual(expected, actual)
