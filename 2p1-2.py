import math


class Rational:
    __num = 1
    __den = 1

    def __init__(self, numerator=1, denominator=1):
        try:
            assert isinstance(numerator, int)
            assert isinstance(denominator, int)
            assert denominator != 0
        except:
            print("Wrong data")
            return
        divisor = math.gcd(numerator, denominator)
        self.__num = numerator // divisor
        self.__den = denominator // divisor

    def show(self):
        return str(self.__num) + '/' + str(self.__den)

    def show_float(self):
        return self.__num / self.__den


a = Rational(-3.7, 4)
print(a.show())
print(a.show_float())
