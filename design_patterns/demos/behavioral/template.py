from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def get_storage_list(self):
        pass

    def save(self, data):
        self.get_storage_list() \
            .append(data)


class SelfListStorage(Storage):
    def __init__(self):
        self.list = []

    def get_storage_list(self):
        return self.list


class ProviderListStorage(Storage):
    def __init__(self, list_provider):
        self.list_provider = list_provider

    def get_storage_list(self):
        return self.list_provider.provide_list()
