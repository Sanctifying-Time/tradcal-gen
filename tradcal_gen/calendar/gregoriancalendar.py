from calendar import monthrange
from datetime import datetime, date

from tradcal_gen.model import FixedLiturgicalDay, CalendarDay, LiturgicalColor

def all_dates_in_year(year):
    for month in range(1, 13): # Month is always 1..12
        for day in range(1, monthrange(year, month)[1] + 1):
            yield date(year, month, day)

class GregorianCalendar:
    DAY_CHRISTMAS = 'chistmas'
    DAY_NEW_YEAR = 'new year'
    DAY_EPIPHANY = 'epiphany'

    fixed_days = {}

    def __init__(self):
        print("Initializing Gregorian Calendar")
        self.fixed_days[self.DAY_CHRISTMAS] = FixedLiturgicalDay(12, 26, "Christmas", LiturgicalColor.WHITE)
        self.fixed_days[self.DAY_NEW_YEAR] = FixedLiturgicalDay(1, 1, "Octave Day of the Nativity of Our Lord", LiturgicalColor.WHITE)
        self.fixed_days[self.DAY_EPIPHANY] = FixedLiturgicalDay(1, 6, "Epiphany", LiturgicalColor.WHITE)

    def generate(self, year=datetime.now().year):
        days = {}
        for date in all_dates_in_year(year):
            days[date] = CalendarDay(date)

        for key, lday in self.fixed_days.items():
            print('Day: {}'.format(key))
            day = days[lday.get_date(year)]
            day.title = lday.title
            day.color = lday.color

        for date, day in days.items():
            print(day)
