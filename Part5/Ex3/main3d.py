#!/usr/bin/python3

import argparse
import cv2
import numpy as np


def onTrackbarminB(minB):
    global minimumB
    minimumB = minB
    print(minB)

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
    parser.add_argument('-hsv ', '--hue_saturation_value', help='To modify the image using HSV instead of BGR',
                        action='store_true')
    args = vars(parser.parse_args())

    # Window name definition
    window_name = 'window - Ex3d'

    # Load image
    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)

    # Show image
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)

    cv2.createTrackbar('Min B', window_name, 0, 255, onTrackbarminB)
    cv2.createTrackbar('Max B', window_name, 0, 255, onTrackbarmaxB)
    cv2.createTrackbar('Min G', window_name, 0, 255, onTrackbarminG)
    cv2.createTrackbar('Max G', window_name, 0, 255, onTrackbarmaxG)
    cv2.createTrackbar('Min R', window_name, 0, 255, onTrackbarminR)
    cv2.createTrackbar('Max R', window_name, 0, 255, onTrackbarmaxR)

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
        cv2.waitKey(1000)



if __name__ == '__main__':
    main()