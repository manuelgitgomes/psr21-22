#!/usr/bin/python3

from time import time, ctime


def sqrts(minnum, maxnum):
    for i in range(minnum, maxnum):
        x = i ** 1/2

    return


def main():
    tic = time()
    minimum_number = 0
    maximum_number = 50000000
    sqrts(minimum_number, maximum_number)
    toc = time()
    time_elapsed = toc - tic
    current_time = ctime()
    print('The time is ' + current_time + '\n' + 'The code ran in ' + str(time_elapsed) + ' seconds.')




if __name__ == '__main__':
    main()