import math


class Rational:
    def __init__(self, num=2, den=4):
        self.__num = num
        self.__den = den

    def check(self):
        return isinstance(self.__num, int) and isinstance(self.__den, int)

    def writing(self):
        if self.check():
            calc = math.gcd(self.__num, self.__den)
            end_num = self.__num / calc
            end_den = self.__den / calc
            return f"{end_num}/{end_den}"
        else:
            return "Enter numbers"

    def writing_float(self):
        if self.check():
            calc = math.gcd(self.__num, self.__den)
            end_num = self.__num / calc
            end_den = self.__den / calc
            return end_num/end_den
        else:
            return "Enter numbers"

    def __add__(self, other):
        if self.check() and other.check():
            calc = math.lcm(self.__den, other.__den)
            s_end_num = self.__num * int(calc / self.__den)
            o_end_num = other.__num * int(calc / other.__den)
            nc_end_num = s_end_num + o_end_num
            f_calc = math.gcd(nc_end_num, calc)
            end_num = nc_end_num / f_calc
            end_den = calc / f_calc
            return f"{end_num}/{end_den}"
        else:
            return "Enter numbers"

    def __sub__(self, other):
        if self.check() and other.check():
            calc = math.lcm(self.__den, other.__den)
            s_end_num = self.__num * int(calc / self.__den)
            o_end_num = other.__num * int(calc / other.__den)
            nc_end_num = s_end_num - o_end_num
            f_calc = math.gcd(nc_end_num, calc)
            end_num = nc_end_num / f_calc
            end_den = calc / f_calc
            return f"{end_num}/{end_den}"
        else:
            return "Enter numbers"

    def __mul__(self, other):
        if self.check() and other.check():
            f_num = self.__num * other.__num
            f_den = self.__den * other.__den
            calc = math.gcd(f_num, f_den)
            end_num = f_num / calc
            end_den = f_den / calc
            return f"{end_num}/{end_den}"
        else:
            return "Enter numbers"

    def __truediv__(self, other):
        if self.check() and other.check():
            f_num = self.__num * other.__den
            f_den = self.__den * other.__num
            calc = math.gcd(f_num, f_den)
            end_num = f_num / calc
            end_den = f_den / calc
            return f"{end_num}/{end_den}"
        else:
            return "Enter numbers"

    def __gt__(self, other):
        if self.check() and other.check():
            calc = math.lcm(self.__den, other.__den)
            s_end_num = self.__num * int(calc / self.__den)
            o_end_num = other.__num * int(calc / other.__den)
            return s_end_num > o_end_num
        else:
            return "Enter numbers"

    def __lt__(self, other):
        if self.check() and other.check():
            calc = math.lcm(self.__den, other.__den)
            s_end_num = self.__num * int(calc / self.__den)
            o_end_num = other.__num * int(calc / other.__den)
            return s_end_num < o_end_num
        else:
            return "Enter numbers"

    def __ge__(self, other):
        if self.check() and other.check():
            calc = math.lcm(self.__den, other.__den)
            s_end_num = self.__num * int(calc / self.__den)
            o_end_num = other.__num * int(calc / other.__den)
            return s_end_num >= o_end_num
        else:
            return "Enter numbers"

    def __le__(self, other):
        if self.check() and other.check():
            calc = math.lcm(self.__den, other.__den)
            s_end_num = self.__num * int(calc / self.__den)
            o_end_num = other.__num * int(calc / other.__den)
            return s_end_num <= o_end_num
        else:
            return "Enter numbers"

    def __eq__(self, other):
        if self.check() and other.check():
            calc = math.lcm(self.__den, other.__den)
            s_end_num = self.__num * int(calc / self.__den)
            o_end_num = other.__num * int(calc / other.__den)
            return s_end_num == o_end_num
        else:
            return "Enter numbers"

    def __ne__(self, other):
        if self.check() and other.check():
            calc = math.lcm(self.__den, other.__den)
            s_end_num = self.__num * int(calc / self.__den)
            o_end_num = other.__num * int(calc / other.__den)
            return s_end_num != o_end_num
        else:
            return "Enter numbers"


x1 = Rational(2, 6)
x2 = Rational(4, 8)
print(x2 != x1)
