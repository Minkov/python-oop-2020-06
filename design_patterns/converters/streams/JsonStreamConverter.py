from json import loads

from converters.streams.StreamConverter import StreamConverter
from file_utils import read_all


class JsonStreamConverter(StreamConverter):
    def convert_from_stream(self, stream):
        return loads(read_all(stream))
