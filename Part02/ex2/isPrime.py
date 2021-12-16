#!/usr/bin/python3


def isPrime(value):
# Calculate the remainder. If it's 0, it's not prime.

    for i in range(2, value):
        remainder = value % i
        if remainder == 0:
            return False

    return True