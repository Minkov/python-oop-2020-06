class ComputerValidator:
    @staticmethod
    def is_valid(computer):
        return computer is not None and \
               computer.ram_in_gb >= 0 and \
               CpuValidator.is_valid(computer.cpu)


class CpuValidator:
    @staticmethod
    def is_valid(cpu):
        return cpu is not None and \
               cpu.number_of_cores > 0
