#!/usr/bin/python3

class ComplexClass:
        def __init__(self, r, i):
            self.r = r
            self.i = i

        def add(self, x):
            a = self.r
            b = self.i
            c = x.r
            d = x.i
            self.r = a + c
            self.i = b + d

        def multiply(self, x):
            a = self.r
            b = self.i
            c = x.r
            d = x.i
            self.r = a * c - b * d
            self.i = a * d + b * c

        def __str__(self):
            a = self.r
            b = self.i
            return str(a) + ' + ' + str(b) + 'j'



def main():

    c1 = ComplexClass(5, 3)
    c2 = ComplexClass(-2, 7)
    print(c1)
    print(c2)
    c1.add(c2)
    print(c1)
    c1.multiply(c2)
    print(c1)

if __name__ == '__main__':
    main()