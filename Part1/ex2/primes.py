#!/usr/bin/python3

def isPrime(value):
# Calculate the remainder. If it's 0, it's not prime.

    for i in range(2, value):
        remainder = value % i
        if remainder == 0:
            return False

    return True


def main():
    # The input is a command that the user can choose the value
    limit = int(input('Maximum value: ')) + 1

    count = 0

    # For every number, it checks if it is prime
    for i in range(1, limit):
        if isPrime(i):
            print('Number ' + str(i) + ' is prime.')
            count += 1
        else:
            print('Number ' + str(i) + ' is not prime.')

    print('From 1 to ' + str(limit - 1) + ', there are ' + str(count) + ' prime numbers')

if __name__ == '__main__':
    main()