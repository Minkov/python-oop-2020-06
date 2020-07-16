class Logger:
    def __init__(self, name):
        self.name = name

    def log(self, text):
        print(text)

class ConsoleLogger(Logger):
    pass

class FileLogger(Logger):
    pass