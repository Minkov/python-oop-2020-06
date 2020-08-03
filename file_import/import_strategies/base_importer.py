from abc import ABC, abstractmethod


class BaseImporter(ABC):
    @abstractmethod
    def get_data_from_stream(self, stream):
        pass