#!/usr/bin/python3

import readchar


def printAllCharsUpTo(stop_char):
    print('Print all values up to ' + stop_char)
    for i in range(ord(' '), ord(stop_char) + 1):
        print(chr(i))


def readAllUpTo(stop_char):
    total_numbers = 0
    total_others = 0



    while True:
        print ('Type something (' + stop_char + ' to stop)')
        pressed_key = readchar.readkey()



        if pressed_key == stop_char:
            print('You pressed ' + pressed_key + '. Goodbye!')
            break
        elif str.isnumeric(pressed_key):
            total_numbers += 1
            print('Thank you for typing ' + pressed_key)
        else:
            total_others += 1
            print('Thank you for typing ' + pressed_key)

    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')

def main():
    # Ex 4a
    # print('Please press a key: ')
    # pressed_char = readchar.readchar()
    # printAllCharsUpTo(pressed_char)

    # Ex 4b
    readAllUpTo('X')

if __name__ == '__main__':
    main()