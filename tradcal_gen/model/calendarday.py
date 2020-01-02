from tradcal_gen.model.liturgicalcolor import LiturgicalColor

class CalendarDay:

    def __init__(self, date):
        self.date = date
        self.title = "Feria"
        self.color = LiturgicalColor.GREEN

    def __str__(self):
        attrs = vars(self)
        return '---\n' + '\n'.join('%s: %s' % item for item in attrs.items()) + '\n'

