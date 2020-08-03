from abc import ABC, abstractmethod


class StreamConverter(ABC):
    @abstractmethod
    def convert_from_stream(self, stream):
        pass