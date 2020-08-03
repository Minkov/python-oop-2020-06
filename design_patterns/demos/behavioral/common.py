from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def can_execute(self):
        pass

class ExitCommand(Command):
    def can_execute(self):
        return True

    def execute(self):
        print('Exiting')

class SaveCommand(Command):
    def __init__(self, storage_dict, *args):
        self.storage_dict = storage_dict
        self.args = args

    def can_execute(self):
        return self.storage_dict is not None

    def execute(self):
        self.storage_dict['values'] = self.args
