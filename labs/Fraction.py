"""
Nate Koch 
"""

class Fraction: # how a class is defined
    
    def __init__(self, num: int, den: int):
        assert num >= 0 and den > 0, "Denominator cannot be 0 and Numerator cannot be negative"
        self.n = num
        self.d = den

    def __str__(self) -> str:
        return f"{self.n}/{self.d}"

    def __repr__(self) -> str:
        return f"Fraction({self.n}, {self.d})"

    def __mul__(self, other: "Fraction") -> "Fraction":
        new_n = self.n * other.n
        new_d = self.d * other.d
        return Fraction(new_n, new_d)

    def __add__(self, other: "Fraction") -> "Fraction":
        new_n = (self.n * other.d) + (other.n * self.d)
        new_d = self.d * other.d
        return Fraction(new_n, new_d)

    def simplify(self) -> "Fraction":
        gcd_val = gcd(self.n, self.d)
        new_n = int(self.n / gcd_val)
        new_d = int(self.d / gcd_val)
        return Fraction(new_n, new_d)

def gcd(a, b) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def main():
    # syntax to create an object
    # ClassName(params, ...)
    f1 = Fraction(5, 7)
    print(f1)
    #print(f1.n)
    #print(f1.d)

    f2 = Fraction(1, 2)
    print(f2)

    mul = f1 * f2
    print("multiplication:", mul)

    add = f1 + f2
    print("addition:", add)

    f3 = Fraction(35, 49)
    simp = f3.simplify()
    print("simplified:", simp)

if __name__ == '__main__':
    main()