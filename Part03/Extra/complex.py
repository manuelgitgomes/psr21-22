#!/usr/bin/python3

def addComplex(x, y):
    """
    Sums the complex number x and y and returns number z
    :param x: a dictionary with 'r' and 'i' as keys and an integer as a value for both
    :param y: same as x
    :return z: same as x
    """
    a = x['r']
    b = x['i']
    c = y['r']
    d = y['i']

    z = {'r': a + c, 'i': b + d}
    return z


def multiplyComplex(x, y):
    """
   Multiplies the complex number x and y and returns number z
   :param x: a dictionary with 'r' and 'i' as keys and an integer as a value for both
   :param y: same as x
   :return z: same as x
   """
    a = x['r']
    b = x['i']
    c = y['r']
    d = y['i']

    z = {'r': a * c - b * d, 'i': a * d + b * c}
    return z

def main():

    complex_dict = {'c1': {'r': 5, 'i': 3}, 'c2': {'r': -2, 'i': 7},
                    'add': lambda x, y: {'r': x['r'] + y['r'], 'i': x['i'] + y['i']}}

    complex_dict['c3'] = {complex_dict['add'](complex_dict['c1'], complex_dict['c2'])}


    return

if __name__ == '__main__':
    main()