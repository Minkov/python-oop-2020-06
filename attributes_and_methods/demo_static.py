result = 0


def add(value):
    global result
    result += value


class MathUtils:
    current_result = 0

    @staticmethod
    def add(value):
        MathUtils.current_result += value

    @staticmethod
    def get_result():
        return MathUtils.current_result


MathUtils.add(5)
print(MathUtils.get_result())
MathUtils.add(3)
print(MathUtils.get_result())
