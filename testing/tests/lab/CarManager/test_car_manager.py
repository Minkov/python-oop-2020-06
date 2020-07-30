import unittest

from lab.CarManager.car_manager import Car


class TestCar(unittest.TestCase):
    def __get_exception_from_init(self, make, model, fuel_consumption, fuel_capacity):
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)
        return context.exception

    def test_carInit_whenValidValues_shouldInitialize(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        car = Car(make, model, fuel_consumption, fuel_capacity)

        expected = [make, model, fuel_consumption, fuel_capacity, 0]
        actual = [car.make, car.model, car.fuel_consumption, car.fuel_capacity, car.fuel_amount]

        self.assertListEqual(expected, actual)

    def test_carInit_whenNoneMake_shouldRaise(self):
        make = None
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenEmptyStringMake_shouldRaise(self):
        make = ''
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenNoneModel_shouldRaise(self):
        make = 'test make'
        model = None
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenEmptyStringModel_shouldRaise(self):
        make = 'test make'
        model = ''
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenNegativeFuelConsumption_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = -1
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenZeroFuelConsumption_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 0
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenNegativeFuelCapacity_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = -1

        params = [make, model, fuel_consumption, fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenZeroFuelCapacity_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 0

        params = [make, model, fuel_consumption, fuel_capacity]

        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_whenNegativeFuelAmount_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        with self.assertRaises(Exception) as context:
            car.fuel_amount = -1

        self.assertIsNotNone(context.exception)

    def test_carRefuel_whenNegativeFuel_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)

        with self.assertRaises(Exception) as context:
            car.refuel(-1)

        self.assertIsNotNone(context.exception)

    def test_carRefuel_whenZeroFuel_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)

        with self.assertRaises(Exception) as context:
            car.refuel(0)

        self.assertIsNotNone(context.exception)

    def test_carRefuel_whenPositiveFuelAndEnoughInCapacity_shouldIncreaseAmount(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        car.refuel(5)

        self.assertEqual(5, car.fuel_amount)

    def test_carRefuel_whenPositiveFuelAndMoreThanCapacity_shouldSetAmountToCapacity(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        car.refuel(car.fuel_capacity * 2)

        self.assertEqual(car.fuel_capacity, car.fuel_amount)

    def test_carDrive_whenEnoughFuel_shouldDecreaseFuel(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)

        car.refuel(car.fuel_capacity)
        distance = 100
        car.drive(distance)
        expected = car.fuel_capacity - car.fuel_consumption * distance / 100
        actual = car.fuel_amount

        self.assertEqual(expected, actual)

    def test_carDrive_whenNotEnoughFuel_shouldRaise(self):
        make = 'test make'
        model = 'test model'
        fuel_consumption = 6
        fuel_capacity = 60

        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)

        with self.assertRaises(Exception) as context:
            car.drive(100)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()
