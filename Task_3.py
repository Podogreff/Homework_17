

class Fraction:
    def __init__(self, num: int, den: int):
        if isinstance(num, (int, float)):
            self.num = num
        else:
            raise ValueError("Please enter int type!")
        if isinstance(den, (int, float)):
            self.den = den
        else:
            raise ValueError("Please enter int type!")

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        gcd = self.greatest_common_divisor(new_num, new_den)
        return Fraction(new_num//gcd, new_den//gcd)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        gcd = self.greatest_common_divisor(new_num, new_den)
        return Fraction(new_num//gcd, new_den//gcd)

    def __mul__(self, other):
        new_num = self.num * other.den * self.den * other.num
        new_den = self.den * other.den
        gcd = self.greatest_common_divisor(new_num, new_den)
        return Fraction(new_num//gcd, new_den//gcd)

    def __truediv__(self, other):
        new_num = (self.num * other.den) / (self.den * other.num)
        new_den = self.den * other.den
        gcd = self.greatest_common_divisor(new_num, new_den)
        return Fraction(new_num//gcd, new_den//gcd)

    def __eq__(self, other):
        num = self.num * other.den
        den = other.num * self.den
        if num == den:
            return f"True! The {Fraction(self.num, self.den)} and {Fraction(other.num, other.den)} are equal"
        return f"False! The {Fraction(self.num, self.den)} and {Fraction(other.num, other.den)} are not equal"

    def __ne__(self, other):
        num = self.num * other.den
        den = other.num * self.den
        if num != den:
            return f"True! The {Fraction(self.num, self.den)} and {Fraction(other.num, other.den)} are not equal"
        return f"False! The {Fraction(self.num, self.den)} and {Fraction(other.num, other.den)} are equal"

    def __lt__(self, other):
        num = self.num * other.den
        den = other.num * self.den
        if num < den:
            return f"True! The {Fraction(self.num, self.den)} < {Fraction(other.num, other.den)}"
        return f"False! The {Fraction(self.num, self.den)} < {Fraction(other.num, other.den)} is not true!"

    def __gt__(self, other):
        num = self.num * other.den
        den = other.num * self.den
        if num > den:
            return f"True! The {Fraction(self.num, self.den)} > {Fraction(other.num, other.den)}"
        return f"False! The {Fraction(self.num, self.den)} > {Fraction(other.num, other.den)} is not true!"

    def __le__(self, other):
        num = self.num * other.den
        den = other.num * self.den
        if num <= den:
            return f"True! The {Fraction(self.num, self.den)} <= {Fraction(other.num, other.den)}"
        return f"False! The {Fraction(self.num, self.den)} <= {Fraction(other.num, other.den)} is not true!"

    def __ge__(self, other):
        num = self.num * other.den
        den = other.num * self.den
        if num >= den:
            return f"True! The {Fraction(self.num, self.den)} >= {Fraction(other.num, other.den)}"
        return f"False! The {Fraction(self.num, self.den)} >= {Fraction(other.num, other.den)} is not true!"

    def greatest_common_divisor(self, num, den):
        while num % den != 0:
            old_num = num
            old_den = den

            num = old_den
            den = old_num % old_den
        return den

    def __str__(self):
        return str(int(self.num)) + "/" + str(int(self.den))


if __name__ == "__main__":
    x = Fraction(2, 5)
    y = Fraction(1, 10)
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)
    print(x == y)
    print(x != y)
    print(x < y)
    print(x > y)
    print(x >= y)
    print(x <= y)


