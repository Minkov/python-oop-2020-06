from import_strategies.csv_importer import CsvImporter
from import_strategies.json_importer import JsonImporter
from import_strategies.primitive_values_importer_decorator import PrimitiveValuesImporterDecorator


class ContentTypeToImporterFactory:
    json_content_types = ('application/json', 'text/json')
    csv_content_types = ('application/vnd.ms-excel',)

    supported_content_types = [*json_content_types, *csv_content_types]

    def get_importer(self, content_type):
        if content_type not in self.supported_content_types:
            raise TypeError('Invalid content type for import')

        if content_type in self.json_content_types:
            return JsonImporter()
        elif content_type in self.csv_content_types:
            return CsvImporter()


class ContentTypeToImporterWithPrimitiveTypesFactory(ContentTypeToImporterFactory):
    def get_importer(self, content_type):
        importer = super().get_importer(content_type)
        return PrimitiveValuesImporterDecorator(importer)
