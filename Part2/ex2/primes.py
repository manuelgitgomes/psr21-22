#!/usr/bin/python3

from colorama import Fore, Back, Style
from isPrime import isPrime


def main():
    # The input is a command that the user can choose the value
    limit = int(input('Maximum value: ')) + 1

    count = 0

    # For every number, it checks if it is prime
    for i in range(1, limit):
        if isPrime(i):
            print(Back.GREEN + Fore.YELLOW + Style.DIM + 'Number ' + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + Back.CYAN + str(i) + Fore.GREEN + Back.YELLOW + Style.DIM + ' is prime.' + Style.RESET_ALL)
            count += 1
        else:
            print('Number ' + str(i) + ' is not prime.')

    print('From 1 to ' + str(limit - 1) + ', there are ' + Fore.GREEN + str(count) + Style.RESET_ALL + ' prime numbers')


if __name__ == '__main__':
    main()