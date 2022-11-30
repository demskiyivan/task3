class Calendar:
    def __init__(self, day, month, year):
        if isinstance(day, int) and isinstance(month, int) and isinstance(year, int) and 0 < month <= 12:
            if month == 4 or month == 6 or month == 9 or month == 10:
                if 0 < day <= 30:
                    self.day = day
                else:
                    raise Exception("Enter valid date")
            elif month == 3:
                if year % 4 == 0:
                    if 0 < day <= 29:
                        self.day = day
                    else:
                        raise Exception("Enter valid date")
                else:
                    if 0 < day <= 28:
                        self.day = day
                    else:
                        raise Exception("Enter valid date")
            else:
                if 0 < day <= 31:
                    self.day = day
                else:
                    raise Exception("Enter valid date")
            self.month = month
            self.year = year
        else:
            raise Exception("Enter valid date")

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

    def __iadd__(self, other):
        if isinstance(other, AddingDate):
            self.day += other.a_day
            self.month += other.a_month
            self.year += other.a_year
            while self.month > 12:
                self.year += 1
                self.month -= 12
            while self.day > 31:
                if self.month > 12:
                    self.year += 1
                    self.month -= 12
                if self.month == 3:
                    if self.year % 4 == 0:
                        self.day -= 29
                    else:
                        self.day -= 28
                elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 10:
                    self.day -= 30
                else:
                    self.day -= 31
                self.month += 1
            if self.month > 12:
                self.year += 1
                self.month -= 12
            if self.month == 3 and self.year % 4 == 0 and self.day > 29:
                self.month += 1
                self.day -= 29
            elif self.month == 3 and self.year % 4 != 0 and self.day > 28:
                self.month += 1
                self.day -= 28
            elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 10 and self.day > 30:
                self.month += 1
                self.day -= 30

    def __isub__(self, other):
        if isinstance(other, AddingDate):
            self.day -= other.a_day
            self.month -= other.a_month
            self.year -= other.a_year
            while self.month < 1:
                self.year -= 1
                self.month += 12
            while self.day < 1:
                if self.month < 1:
                    self.year -= 1
                    self.month += 12
                if self.month == 3:
                    if self.year % 4 == 0:
                        self.day += 29
                    else:
                        self.day += 28
                elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 10:
                    self.day += 30
                else:
                    self.day += 31
            if self.month > 12:
                self.year += 1
                self.month -= 12
            if self.month == 3 and self.year % 4 == 0 and self.day > 29:
                self.month += 1
                self.day -= 29
            elif self.month == 3 and self.year % 4 != 0 and self.day > 28:
                self.month += 1
                self.day -= 28
            elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 10 and self.day > 30:
                self.month += 1
                self.day -= 30

    def __gt__(self, other):
        if isinstance(other, Calendar):
            if self.year > other.year and self.month > other.month and self.day > other.day:
                return True
            else:
                return False
        else:
            raise Exception("Compare two calendars")

    def __lt__(self, other):
        if isinstance(other, Calendar):
            if self.year < other.year and self.month < other.month and self.day < other.day:
                return True
            else:
                return False
        else:
            raise Exception("Compare two calendars")

    def __ge__(self, other):
        if isinstance(other, Calendar):
            if self.year >= other.year and self.month >= other.month and self.day >= other.day:
                return True
            else:
                return False
        else:
            raise Exception("Compare two calendars")

    def __le__(self, other):
        if isinstance(other, Calendar):
            if self.year <= other.year and self.month <= other.month and self.day <= other.day:
                return True
            else:
                return False
        else:
            raise Exception("Compare two calendars")

    def __eq__(self, other):
        if isinstance(other, Calendar):
            if self.year == other.year and self.month == other.month and self.day == other.day:
                return True
            else:
                return False
        else:
            raise Exception("Compare two calendars")

    def __ne__(self, other):
        if isinstance(other, Calendar):
            if self.year != other.year and self.month != other.month and self.day != other.day:
                return True
            else:
                return False
        else:
            raise Exception("Compare two calendars")

        
class AddingDate:
    def __init__(self, day, month, year):
        if isinstance(day, int) and isinstance(month, int) and isinstance(year, int):
            if day >= 0 and month >= 0 and year >= 0:
                self.a_day = day
                self.a_month = month
                self.a_year = year
            else:
                raise Exception("Enter positive number")
        else:
            raise Exception("Enter Number")

    def __str__(self):
        return f'{self.a_day}.{self.a_month}.{self.a_year}'
