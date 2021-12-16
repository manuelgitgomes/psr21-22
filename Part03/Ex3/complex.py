#!/usr/bin/python3

from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])

def addComplex(x, y):
    # add complex numbers
    z = Complex(x.r + y.r, x.i + y.i)
    return z

def multiplyComplex(x, y):
    # multiply complex number
    z = Complex(x.r * y.r - x.i * y.i, x.r * y.i + x.i * y.r)
    return z

def printComplex(x):
    # print complex number
    print('The complex number is ' + str(x.r) + ' + ' + str(x.i) + 'j')

def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()