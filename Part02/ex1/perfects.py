#!/usr/bin/python3

from colorama import Fore, Back, Style

def getDividers(value):
    """
    Return a list of dividers for the number value
    :param value: the number to test
    :return: a list of dividers.
    """
    dividers = []

    for i in range(1, value):
        remainder = value % i
        if remainder == 0:
            dividers.append(i)


    return dividers



def isPerfect(value, dividers):
    """
    Checks whether the number value is perfect.
    :param value: the number to test.
    :return: True or False
    """
# Calculate the remainder. If it's 0, it's not prime.
    perfectSum = sum(dividers)

    if value == perfectSum:
        return True
    else:
        return False



def main():
    # The input is a command that the user can choose the value
    limit = int(input('Maximum value: ')) + 1

    perfects = []

    count = 0

    # For every number, it checks if it is prime
    for i in range(1, limit):
        dividers = getDividers(i)
        print('The dividers for ' + str(i) + ' are ' + str(dividers))

        if isPerfect(i, dividers):
            print(Fore.GREEN + 'Number '+ str(i) + ' is perfect.' + Style.RESET_ALL)
            count += 1
            perfects.append(i)
        else:
            print('Number ' + str(i) + ' is not perfect.')

    print('From 1 to ' + str(limit - 1) + ', there are ' + Fore.GREEN + str(count) + Style.RESET_ALL + ' perfect numbers, who are ' + str(perfects))

if __name__ == '__main__':
    main()