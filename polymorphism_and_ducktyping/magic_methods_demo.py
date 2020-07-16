# 1/3

# f1 + f2 * f3 / f4


from math import gcd


def simplify(numerator, denominator):
    the_gcd = gcd(numerator, denominator)
    return (numerator // the_gcd, denominator // the_gcd)


class Fraction():
    def __init__(self, numerator, denominator):
        (numerator, denominator) = simplify(numerator, denominator)
        self.numerator = numerator
        self.denominator = denominator

    def to_number(self):
        return self.numerator / self.denominator

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'

    def __add__(self, other):
        """
        1     3       1 * 4 + 3 * 2
        -  +  -   =   -------------
        2     4           2 * 4
        """
        numerator = self.numerator * other.denominator + \
                    other.numerator * self.denominator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __mul__(self, other):
        """
        1     3       1 * 3
        -  *  -   =   -----
        2     4       2 * 4
        """
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __gt__(self, other):
        numerator1 = self.numerator * other.denominator
        numerator2 = other.numerator * self.denominator

        return numerator2 > numerator1

    def __ge__(self, other):
        return other.to_number() >= self.to_number()


f1 = Fraction(1, 2)
f2 = Fraction(3, 4)

print(f1)
print(f2)

print(f1 + f2)
print(f1 * f2)

f1 += 5
print(f1)
print(f1 + 5)

dir(f1)

print(2 + 3)
print(1 / 2 + 3 / 4)

print(dir(int))

print(dir(Fraction))

f1 = Fraction(1, 2)
f2 = Fraction(3, 4)

print(f1 > f2)
print(f2 > f1)
print(f1 >= f2)
print(f1 < f2)
