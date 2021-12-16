#!/usr/bin/python3

from functools import partial
import argparse
import cv2


def onTrackbar(threshold, window_name, image_gray):
    # The value of the threshold of the binarization is the one on the trackbar
    _, dst = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, dst)

def onMouse(curr, posx, posy, last, a):
    if curr == 1:
        print('The position of your cursor is: (' + str(posx) + ', ' + str(posy) + ')')


def main():
    # Create parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-img', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    # Window name definition
    window_name = 'window - Ex3b'

    # Load image
    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)

    # Convert to grey and use as a global variable
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Show grey image
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image_gray)

    # Create the mouse callback
    cv2.setMouseCallback(window_name, onMouse)

    # Using partial
    onTrackbarLite = partial(onTrackbar, window_name=window_name, image_gray=image_gray)

    # Create trackbar to binarize image
    cv2.createTrackbar('Threshold', window_name, 0, 255, onTrackbarLite)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()