from abc import ABC, abstractmethod


class FileSystemItem(ABC):
    @abstractmethod
    def get_size(self):
        pass


class File(FileSystemItem):
    def get_size(self):
        return 13


class Directory(FileSystemItem):
    def __init__(self, files, directories):
        self.files = files
        self.directories = directories

    def get_size(self):
        return sum(file.get_size() for file in self.files) + \
               sum(dir.get_size() for dir in self.directories)
