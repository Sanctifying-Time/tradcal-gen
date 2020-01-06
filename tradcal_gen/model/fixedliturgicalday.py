from datetime import date

from tradcal_gen.model.liturgicalday import LiturgicalDay

class FixedLiturgicalDay(LiturgicalDay):

	def __init__(self, month, day, title, color):
		self.month = month
		self.day = day
		self.title = title
		self.color = color

	def get_date(self, year):
		return date(year, self.month, self.day)