#!/usr/bin/python3

import argparse
import cv2
import numpy as np
import json


# Creating a function for each trackbar to store their values to a global variable
def onTrackbarminB(minB):
    global minimumB
    minimumB = minB


def onTrackbarmaxB(maxB):
    global maximumB
    maximumB = maxB


def onTrackbarminG(minG):
    global minimumG
    minimumG = minG


def onTrackbarmaxG(maxG):
    global maximumG
    maximumG = maxG


def onTrackbarminR(minR):
    global minimumR
    minimumR = minR


def onTrackbarmaxR(maxR):
    global maximumR
    maximumR = maxR


def main():
    # Global variables
    global minimumB, minimumG, minimumR, maximumB, maximumG, maximumR

    minimumB = 0
    minimumG = 0
    minimumR = 0
    maximumB = 255
    maximumG = 255
    maximumR = 255

    # Create parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-img', '--image', type=str, required=True, help='Full path to image file.')
    parser.add_argument('-hsv', '--hue_saturation_value', help='To modify the image using HSV instead of BGR',
                        action='store_true')
    args = vars(parser.parse_args())

    # Window name definition
    window_name = 'window - Ex3d'

    # Load image
    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)

    # If the hsv mode is selected, convert the image
    if args['hue_saturation_value']:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Show image
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)

    # Create all trackbar
    cv2.createTrackbar('Min B/H', window_name, 0, 255, onTrackbarminB)
    cv2.createTrackbar('Max B/H', window_name, 0, 255, onTrackbarmaxB)
    cv2.createTrackbar('Min G/S', window_name, 0, 255, onTrackbarminG)
    cv2.createTrackbar('Max G/S', window_name, 0, 255, onTrackbarmaxG)
    cv2.createTrackbar('Min R/V', window_name, 0, 255, onTrackbarminR)
    cv2.createTrackbar('Max R/V', window_name, 0, 255, onTrackbarmaxR)

    # While cycle to create a mask according to the values on the trackbars
    while True:
        ranges = {'limits': {'b': {'max': maximumB, 'min': minimumB},
                             'g': {'max': maximumG, 'min': minimumG},
                             'r': {'max': maximumR, 'min': minimumR}}}

        mins = np.array([ranges['limits']['b']['min'], ranges['limits']['g']['min'], ranges['limits']['r']['min']])
        maxs = np.array([ranges['limits']['b']['max'], ranges['limits']['g']['max'], ranges['limits']['r']['max']])
        mask = cv2.inRange(image, mins, maxs)

        # Show image
        cv2.namedWindow(window_name)
        cv2.imshow(window_name, mask)
        key = cv2.waitKey(1)

        # If you press q, the program shuts down and saves the final directory
        if key == ord('q'):
            print('Program ending, saving dictionary')
            file_name = 'limits.json'
            with open(file_name, 'w') as file_handle:
                print('Writing dictionary ranges to file ' + file_name)
                json.dump(ranges, file_handle)  # d is the dictionary
                break


if __name__ == '__main__':
    main()