from mixins.debug_attributes_setter_mixin import DebugAttributesSetterMixin
from mixins.print_state_mixin import PrintStateMixin


class NumbersFormatter:
    def to_2digit_number(self, number):
        return f'{number:02d}'


class MonthsFormatter:
    def get_name(self, month_index):
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        return month_names[month_index - 1]


class Clock():
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.numbersFormatter = NumbersFormatter()

    @property
    def time(self):
        hours_formatted = self.numbersFormatter.to_2digit_number(self.hours)
        minutes_formatted = self.numbersFormatter.to_2digit_number(self.minutes)
        seconds_formatted = self.numbersFormatter.to_2digit_number(self.seconds)
        return f'{hours_formatted}:{minutes_formatted}:{seconds_formatted}'


class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.months_formatter = MonthsFormatter()

    @property
    def date(self):
        return f'{self.year}/{self.months_formatter.get_name(self.month)}/{self.day}'

    def __repr__(self):
        return self.date


class CalendarClock(Calendar, Clock, DebugAttributesSetterMixin):
    def __init__(self, year, month, day, hours, minutes, seconds):
        Calendar.__init__(self, year, month, day)
        Clock.__init__(self, hours, minutes, seconds)

    @property
    def datetime(self):
        return f'{self.date} {self.time}'

    def __repr__(self):
        calendar_repr = Calendar.__repr__(self)
        clock_repr = Clock.__repr__(self)
        return f'{calendar_repr} {clock_repr}'


clock = Clock(19, 9, 50)
calendar = Calendar(2020, 7, 13)
cc = CalendarClock(2020, 6, 13, 19, 9, 1)

print(clock)
print(calendar)
print(cc)

print(Clock.mro())
print(CalendarClock.mro())

clock.print_state()
