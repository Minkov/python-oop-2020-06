class DebugAttributesSetterMixin:
    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        print(f'{self.__class__}, {key}={value}')
