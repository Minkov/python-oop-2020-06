from computer_validators import CpuValidator


class Cpu:
    def __init__(self, manufacturer, model, number_of_cores):
        self.manufacturer = manufacturer
        self.model = model
        self.number_of_cores = number_of_cores

class Computer:
    def __init__(self, cpu, ram_in_gb):
        if not Computer.is_valid_ram(ram_in_gb):
            raise ValueError('Invalid RAM')

        # cpu_validator.is_valid(cpu)
        self.cpu = cpu
        self.ram_in_gb = ram_in_gb

    @staticmethod
    def is_valid_ram(ram_in_gb):
        return ram_in_gb >= 0

    @classmethod
    def from_string(cls, computer_string):
        # {cpu_manufacturer};{cpu_model};{cpu_number_of_cores};{ram_in_gb}
        print(' --- From classmethod ---')
        print(cls.__dict__)
        (cpu_manufacturer, cpu_model, cpu_number_of_cores, ram_in_gb) \
            = computer_string.split(';')
        cpu = Cpu(cpu_manufacturer, cpu_model, cpu_number_of_cores)
        return cls(cpu, int(ram_in_gb))

    def get_details(self):
        return f'{self.cpu.number_of_cores}-core processor and {self.ram_in_gb}GB RAM'
    # def __setattr__(self, key, value):
    #     b = 5

    def __getattr__(self, item):
        pass

    def __delattr__(self, item):
        pass

cpu = Cpu('Intel', 'i7', 6)

rog = Computer(cpu, 16)
#
# print(rog.cpu)
# print(rog.ram_in_gb)
# print(rog.get_details())
# print(rog.__dict__)
# print(Computer.__dict__)

def print_attributes(obj, offset=''):
    # has_model = hasattr(obj, 'model')
    # print(f'{offset}Has model? -> {has_model}')
    # if 'model' in obj.__dict__:
    #     print(f'{offset}Has model')
    # else:
    #     print(f'{offset}No model')
    # print(obj.model)
    for key in obj.__dict__.keys():
        value = getattr(obj, key)
        if isinstance(value, int) or isinstance(value, str):
            print(f'{offset}{key}={value}')
        else:
            print(f'{offset}{key}')
            print_attributes(value, offset + '  ')

rog2 = Computer.from_string('AMD;Ryzen 7;8;32')
print_attributes(rog2)