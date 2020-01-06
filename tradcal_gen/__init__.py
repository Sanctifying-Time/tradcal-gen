from ._version import __version__

from .calendar import Latin1962

def main(): # pragma: no cover
    print('Hello, Trads!')
    Latin1962().generate(2020)

