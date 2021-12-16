#!/usr/bin/python3

def addComplex(x, y):
    # add complex numbers
    z = (x[0] + y[0], x[1] + y[1])
    return z

def multiplyComplex(x, y):
    # multiply complex number
    z = (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])
    return z

def printComplex(x):
    # print complex number
    print('The complex number is ' + str(x[0]) + ' + ' + str(x[1]) + 'j')

def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()