#mostly chatGPT
class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator can not be zero")
        elif not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise ValueError("Numerator and denominator must be whole numbers")
        elif not isinstance(numerator, int) or not isinstance(denominator, int):
            numerator, denominator = self._convert_to_int(numerator, denominator)
        else:
            pass

        common = self._gcd(numerator, denominator)
        self.numerator = int(numerator) // common
        self.denominator = int(denominator) // common

    @staticmethod
    def _convert_to_int(num1, num2):
        num1, num2 = float(num1), float(num2)
        mult = 10 ** max(len(str(num1).split('.')[1]), len(str(num2).split('.')[1]))
        num1 *= mult
        num2 *= mult
        return int(num1), int(num2)

    @staticmethod
    def _gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __add__(self, other):
        sum_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        sum_denominator = self.denominator * other.denominator
        return Fraction(sum_numerator, sum_denominator)

    def __sub__(self, other):
        sum_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        sum_denominator = self.denominator * other.denominator
        return Fraction(sum_numerator, sum_denominator)

    def __mul__(self, other):
        mul_numerator = self.numerator * other.numerator
        mul_denominator = self.denominator * other.denominator
        return Fraction(mul_numerator, mul_denominator)

    def __truediv__(self, other):
        div_numerator = self.numerator * other.denominator
        div_denominator = self.denominator * other.numerator
        return Fraction(div_numerator, div_denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            other = Fraction(other)
        return self.numerator == other.numerator and self.denominator == other.denominator


x = Fraction(1/2)
y = Fraction(1/4)

print(x)
print(y)


assert x + y == Fraction(3/4)
