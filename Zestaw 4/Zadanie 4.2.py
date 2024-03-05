import cmath
from math import hypot, atan


class Zespolona:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def conjugate(self):
        return self.__class__(self.r, -self.i)

    def argz(self):
        return atan(self.i / self.r)

    def __abs__(self):
        return hypot(self.r, self.i)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.r}, {self.i})"

    def __str__(self):
        return f"({self.r}{self.i:+}j)"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.r + other.r, self.i + other.i)
        elif isinstance(other, (int, float)):
            return self.__class__(self.r + other, self.i)
        elif isinstance(other, complex):
            return self.__class__(self.r + other.real, self.i + other.imag)
        else:
            raise TypeError("Nieprawidłowy typ")


    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.r - other.r, self.i - other.i)
        elif isinstance(other, (int, float)):
            return self.__class__(self.r - other, self.i)
        elif isinstance(other, complex):
            return self.__class__(self.r - other.real, self.i - other.imag)
        else:
            raise TypeError("Nieprawidłowy typ")

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.r * other.r - self.i * other.i,
                                self.r * other.i + self.i * other.r)
        elif isinstance(other, (int, float)):
            return self.__class__(self.r * other, self.i * other)
        elif isinstance(other, complex):
            return self.__class__(self.r * other.real - self.i * other.imag,
                                self.r * other.imag + self.i * other.real)
        else:
            raise TypeError("Nieprawidłowy typ")

    def __radd__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.r + other.r, self.i + other.i)
        elif isinstance(other, (int, float)):
            return self.__class__(self.r + other, self.i)
        elif isinstance(other, complex):
            return self.__class__(self.r + other.real, self.i + other.imag)
        else:
            raise TypeError("Nieprawidłowy typ")

    def __rmul__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.r * other.r , self.i )
        elif isinstance(other, (int, float)):
            return self.__class__(self.r * other, self.i)
        elif isinstance(other, complex):
            return self.__class__(self.r * other.real, self.i )
        else:
            raise TypeError("Nieprawidłowy typ")

    def __rsub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(other.r - self.r, -self.i)
        elif isinstance(other, (int, float)):
            return self.__class__(other - self.r, -self.i)
        elif isinstance(other, complex):
            return self.__class__(other.real - self.r, -self.i)
        else:
            raise TypeError("Nieprawidłowy typ")

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.r == other.r and self.i == other.i
        elif isinstance(other, (int, float)):
            return self.r == other and self.i == 0
        elif isinstance(other, complex):
            return self.r == other.real and self.i == other.imag
        else:
            raise TypeError("Nieprawidłowy typ")


    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.r != other.r or self.i != other.i
        elif isinstance(other, (int, float)):
            return self.r != other or self.i != 0
        elif isinstance(other, complex):
            return self.r != other.real or self.i != other.imag
        else:
            raise TypeError("Nieprawidłowy typ")

    def __pow__(self, other):
        r = abs(self)
        theta = self.argz()
        new_r = r ** other
        new_theta = theta * other
        real_part = (new_r * cmath.cos(new_theta))
        imag_part = (new_r * cmath.sin(new_theta))
        real_part = round(real_part.real, 2)
        imag_part = round(imag_part.real, 2)
        return self.__class__(real_part, imag_part)


def main():
    print("Liczby zespolone")
    a = Zespolona(2, 5)
    b = Zespolona(1, -3)
    print(a)
    print(b)
    b_copy = eval(repr(b))
    print(type(b_copy), b_copy.r, b_copy.i)
    print(a + b)
    print(a - b)
    print(a + 4)
    print(7 - a)
    print(a * 4)
    print(a * (-4))
    print(a == Zespolona(2, 5))
    print(a == b)
    print(a != b)
    print(a != Zespolona(2, 5))
    print(a ** 2)
    print(b ** 4)


if __name__ == "__main__":
    main()

# Liczby zespolone
# (2+5j)
# (1-3j)
# <class '__main__.Zespolona'> 1 -3
# (3+2j)
# (1+8j)
# (6+5j)
# (5-5j)
# (8+20j)
# (-8-20j)
# True
# False
# True
# False
# (-21+20j)
# (28+96j)


