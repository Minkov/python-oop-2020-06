from csv import reader
from io import StringIO

from converters.streams.StreamConverter import StreamConverter
from file_utils import read_all


class CsvStreamConverter(StreamConverter):
    def convert_from_stream(self, stream):
        text = read_all(stream)

        string_stream = StringIO(text)
        csv_reader = reader(string_stream)

        rows = [row for row in csv_reader]

        dd = {rows[0][i].strip(): rows[1][i].strip() for i in range(len(rows[0]))}

        return dd
