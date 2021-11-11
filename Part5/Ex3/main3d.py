#!/usr/bin/python3

import copy
import argparse
import cv2
import numpy as np
from functools import partial


def onTrackbar(minimumB, maximumB, minimumG, maximumG, minimumR, maximumR, window_name, image_bgr, hsv):
    dic = {'limits': {'B': {'max': maximumB, 'min': minimumB},
                      'G': {'max': maximumG, 'min': minimumG},
                      'R': {'max': maximumR, 'min': minimumR}}}



def main():
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

    # Create partial functions
    onTrackbarLite = partial(onTrackbar, window_name=window_name, image_bgr=image, hsv=args['hue_saturation_value'])
    onTrackbarBmin = partial(onTrackbarLite, maximumB=0, maximumG=0, maximumR=0, minimumR=0, minimumG=0)
    onTrackbarBmax = partial(onTrackbarLite, minimumB=0, maximumG=0, maximumR=0, minimumR=0, minimumG=0)
    onTrackbarGmin = partial(onTrackbarLite, maximumG=0, maximumB=0, maximumR=0, minimumR=0, minimumB=0)
    onTrackbarGmax = partial(onTrackbarLite, maximumB=0, minimumG=0, maximumR=0, minimumR=0, minimumB=0)
    onTrackbarRmin = partial(onTrackbarLite, maximumR=0, maximumG=0, maximumB=0, minimumB=0, minimumG=0)
    onTrackbarRmax = partial(onTrackbarLite, maximumB=0, maximumG=0, minimumB=0, minimumR=0, minimumG=0)


    cv2.createTrackbar('Min B', window_name, 0, 255, onTrackbarBmin)
    cv2.createTrackbar('Max B', window_name, 0, 255, onTrackbarBmax)
    cv2.createTrackbar('Min G', window_name, 0, 255, onTrackbarGmin)
    cv2.createTrackbar('Max G', window_name, 0, 255, onTrackbarGmax)
    cv2.createTrackbar('Min R', window_name, 0, 255, onTrackbarRmin)
    cv2.createTrackbar('Max R', window_name, 0, 255, onTrackbarRmax)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()