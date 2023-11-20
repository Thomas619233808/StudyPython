class Fraction:
    def __init__(self, a,  b):
        self.a = a
        self.b = b
        x = self.gcd(a, b)
        self.a /= x
        self.b /= x

    def gcd(self, a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    def zgs(self, a, b):
        # 12 15 -> 4
        # 3*4*4=48
        x = self.gcd(a,b )
        return a * b / x

    def __add__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        fenmu = self.zgs(b, d)
        fenzi = a * fenmu / b + c * fenmu / d
        return Fraction(fenzi, fenmu)

    def __str__(self):
        return "%d/%d" % (self.a, self.b)



f = Fraction(30, 15)
print(f)