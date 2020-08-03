class IPrintAttributes:
    def __str__(self):
        pairs = [f'{key}={value}' for (key, value) in self.__dict__.items()]
        return '; '.join(pairs)
