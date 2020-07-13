class PrintStateMixin:
    def print_state(self):
        print(f' --- {self.__class__} ---')
        for (key, value) in self.__dict__.items():
            print(f'{key}={value}')

        print(f' -----------')

    def __repr__(self):
        lines = []
        lines.append(f' --- {self.__class__} ---')
        for (key, value) in self.__dict__.items():
            lines.append(f'{key}={value}')

        lines.append(f' -----------')
        return '\n'.join(lines)
