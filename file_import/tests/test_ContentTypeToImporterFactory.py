from unittest import TestCase

from factories.ContentTypeToImporterFactory import ContentTypeToImporterFactory
from import_strategies.csv_importer import CsvImporter
from import_strategies.json_importer import JsonImporter


class TestContentTypeToImporterFactory(TestCase):
    def setUp(self) -> None:
        self.factory = ContentTypeToImporterFactory()

    def test_getImporter_whenContentTypeIsCsv_shouldReturnCsvImporter(self):
        importer = self.factory.get_importer(self.factory.csv_content_types[0])

        self.assertEqual(CsvImporter, importer.__class__)

    def test_getImporter_whenContentTypeIsJson_shouldReturnJsonImporter(self):
        importer = self.factory.get_importer(self.factory.json_content_types[0])

        self.assertEqual(JsonImporter, importer.__class__)

    def test_getImporter_whenContentTypeIsInvalid_shouldRaise(self):
        with self.assertRaises(TypeError) as context:
            self.factory.get_importer('text/plain')

        self.assertIsNotNone(context.exception)
