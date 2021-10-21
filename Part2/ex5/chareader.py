#!/usr/bin/python3

import readchar
from colorama import Fore, Style

def printAllCharsUpTo(stop_char):
    print('Print all values up to ' + stop_char)
    for i in range(ord(' '), ord(stop_char) + 1):
        print(chr(i))


def readAllUpTo(stop_char):
    pressed_keys = []
    pressed_numbers = []
    pressed_others = []

    total_numbers = 0
    total_others = 0
    counter = 0

    while True:
        print ('Type something (' + stop_char + ' to stop)')
        pressed_key = readchar.readkey()

        if pressed_key == stop_char:
            print('You pressed ' + pressed_key + '. Goodbye!')
            break
        else:
            print('Thank you for typing ' + pressed_key)
            pressed_keys.append(pressed_key)

    for pressed_key in pressed_keys:
        if str.isnumeric(pressed_key):
            total_numbers += 1
            pressed_numbers.append(pressed_key)
        else:
            total_others += 1
            pressed_others.append(pressed_key)

    print('You entered ' + str(total_numbers) + ' numbers, which are: ' + str(pressed_numbers))
    print('You entered ' + str(total_others) + ' others, which are: ' + str(pressed_others))

    # Colored text

    coloursList = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.YELLOW, Fore.CYAN];

    printStr = 'Colour party! '

    for other in pressed_others:
        printStr = printStr + coloursList[counter] + str(other) + Style.RESET_ALL
        if counter >= len(coloursList)-1:
            counter = 0
        else:
            counter += 1

    print(printStr)


def main():
    # Ex 4a
    # print('Please press a key: ')
    # pressed_char = readchar.readchar()
    # printAllCharsUpTo(pressed_char)

    # Ex 4b
    readAllUpTo('X')

if __name__ == '__main__':
    main()