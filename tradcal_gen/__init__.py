from ._version import __version__

from collections import namedtuple
from calendar import monthrange
import datetime
from .model import CalendarDay

def all_dates_in_year(year):
    for month in range(1, 13): # Month is always 1..12
        for day in range(1, monthrange(year, month)[1] + 1):
            yield datetime.date(year, month, day)

def main(): # pragma: no cover
    print('Hello, Trads!')

    days = []
    for date in all_dates_in_year(2020):
        day = CalendarDay(date)
        days.append(day)
        print(day)
